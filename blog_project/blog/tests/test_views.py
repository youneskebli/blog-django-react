from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from blog.models import Article, Writer
from django.utils import timezone
from django.contrib.auth.models import User


class DashboardAPIViewTests(APITestCase):

    def setUp(self):
        self.writer = Writer.objects.create(user=self.create_user(), name="Writer 1")
        self.url = reverse("dashboard")

    def create_user(self):
        return User.objects.create_user(username="writer1", password="password")

    def test_dashboard_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_dashboard_authenticated(self):
        self.client.force_authenticate(user=self.writer.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dashboard_article_counts(self):
        self.client.force_authenticate(user=self.writer.user)
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        Article.objects.create(
            title="Test Article", written_by=self.writer, created_at=timezone.now()
        )
        Article.objects.create(
            title="Old Article",
            written_by=self.writer,
            created_at=thirty_days_ago - timezone.timedelta(days=1),
        )

        response = self.client.get(self.url)
        data = response.json()
        self.assertEqual(data[0]["total_articles"], 2)
        self.assertEqual(data[0]["articles_last_30_days"], 1)


class ArticleCreateAPIViewTests(APITestCase):

    def setUp(self):
        self.writer = Writer.objects.create(user=self.create_user(), name="Writer 1")
        self.url = reverse("article-create")

    def create_user(self):
        return User.objects.create_user(username="writer1", password="password")

    def test_create_article_unauthenticated(self):
        response = self.client.post(self.url, {"title": "New Article"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_article_authenticated(self):
        self.client.force_authenticate(user=self.writer.user)
        response = self.client.post(
            self.url, {"title": "New Article", "content": "Content"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_article_missing_fields(self):
        self.client.force_authenticate(user=self.writer.user)
        response = self.client.post(self.url, {"title": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIViewTests(APITestCase):

    def setUp(self):
        self.writer = Writer.objects.create(user=self.create_user(), name="Writer 1")
        self.editor = Writer.objects.create(
            user=self.create_user("editor"), name="Editor", is_editor=True
        )
        self.article = Article.objects.create(
            title="Test Article", written_by=self.writer
        )
        self.url = reverse("article-detail", kwargs={"id": self.article.id})

    def create_user(self, username="writer1"):
        return User.objects.create_user(username=username, password="password")

    def test_get_article_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_article_authenticated_writer(self):
        self.client.force_authenticate(user=self.writer.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_article_authenticated_editor(self):
        self.client.force_authenticate(user=self.editor.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_article_readonly_status(self):
        self.client.force_authenticate(user=self.writer.user)
        response = self.client.patch(self.url, {"status": "APPROVED"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_article_content(self):
        self.client.force_authenticate(user=self.writer.user)
        response = self.client.patch(self.url, {"content": "Updated Content"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ArticleApprovalAPIViewTests(APITestCase):

    def setUp(self):
        self.editor = Writer.objects.create(
            user=self.create_user("editor"), name="Editor", is_editor=True
        )
        self.article = Article.objects.create(
            title="Test Article", status=Article.Status.PENDING
        )
        self.url = reverse("article-approval", kwargs={"article_id": self.article.id})

    def create_user(self, username):
        return User.objects.create_user(username=username, password="password")

    def test_approve_article(self):
        self.client.force_authenticate(user=self.editor.user)
        response = self.client.post(self.url, {"action": "approve"})
        self.article.refresh_from_db()
        self.assertEqual(self.article.status, Article.Status.APPROVED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reject_article(self):
        self.client.force_authenticate(user=self.editor.user)
        response = self.client.post(self.url, {"action": "reject"})
        self.article.refresh_from_db()
        self.assertEqual(self.article.status, Article.Status.REJECTED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_action(self):
        self.client.force_authenticate(user=self.editor.user)
        response = self.client.post(self.url, {"action": "invalid_action"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ArticlesEditedAPIViewTests(APITestCase):

    def setUp(self):
        self.editor = Writer.objects.create(
            user=self.create_user("editor"), name="Editor", is_editor=True
        )
        self.url = reverse("articles-edited")

    def create_user(self, username):
        return User.objects.create_user(username=username, password="password")

    def test_get_edited_articles(self):
        self.client.force_authenticate(user=self.editor.user)
        Article.objects.create(
            title="Approved Article",
            edited_by=self.editor,
            status=Article.Status.APPROVED,
        )
        Article.objects.create(
            title="Rejected Article",
            edited_by=self.editor,
            status=Article.Status.REJECTED,
        )

        response = self.client.get(self.url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["status"], Article.Status.APPROVED)
        self.assertEqual(data[1]["status"], Article.Status.REJECTED)
