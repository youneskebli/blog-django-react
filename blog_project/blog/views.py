from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, Writer
from .serializers import ArticleSerializer
from django.db.models import Count, Q
from django.utils import timezone


class DashboardAPIView(generics.ListAPIView):
    permission_classes = [
        AllowAny,
    ]
    queryset = Article.objects.all()

    def get(self, request, *args, **kwargs):
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        stats = Writer.objects.annotate(
            total_articles=Count("articles_written"),
            articles_last_30_days=Count(
                "articles_written",
                filter=Q(articles_written__created_at__gte=thirty_days_ago),
            ),
        ).values("name", "total_articles", "articles_last_30_days")
        return Response(stats)


class ArticleCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(written_by=self.request.user.writer)


class ArticleDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Article.objects.filter(written_by=self.request.user.writer)

    def patch(self, request, *args, **kwargs):
        if "status" in request.data:
            return Response(
                {"error": "Status field is read-only"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        allowed_fields = ["title", "content"]
        for field in request.data:
            if field not in allowed_fields:
                return Response(
                    {"error": f'Field "{field}" is not editable'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return self.partial_update(request, *args, **kwargs)


class ArticleApprovalAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        articles = Article.objects.filter(status=Article.Status.PENDING)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, article_id):
        print(request)
        article = Article.objects.get(id=article_id)
        action = request.data.get("action")
        if action in ["approve", "reject"]:
            article.status = (
                Article.Status.APPROVED
                if action == "approve"
                else Article.Status.REJECTED
            )
            article.edited_by = request.user.writer
            article.save()
            return Response({"status": "success"})
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)


class ArticlesEditedAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(
            edited_by=self.request.user.writer,
            status__in=[Article.Status.APPROVED, Article.Status.REJECTED],
        )
