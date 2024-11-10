from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Q
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Article, Writer
from .serializers import ArticleSerializer, ArticleDetailSerializer
from .permissions import IsWriterOrEditor, IsEditor, IsWriter


# Dashboard View: Writer Summary
class DashboardAPIView(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)

        writer_stats = Writer.objects.annotate(
            total_articles=Count("articles_written"),
            articles_last_30_days=Count(
                "articles_written",
                filter=Q(articles_written__created_at__gte=thirty_days_ago)
            )
        ).values("name", "total_articles", "articles_last_30_days")

        return Response(writer_stats)

class ArticleCreateAPIView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated, IsWriter]
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):

        serializer.save(written_by=self.request.user.writer)


class ArticleDetailAPIView(generics.RetrieveUpdateAPIView):

    permission_classes = [IsAuthenticated, IsWriterOrEditor]
    serializer_class = ArticleDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):

        if self.request.user.writer.is_editor:
            return Article.objects.all()
        return Article.objects.filter(written_by=self.request.user.writer)

    def patch(self, request, *args, **kwargs):

        if "status" in request.data:
            return Response({"error": "Status field is read-only"}, status=status.HTTP_400_BAD_REQUEST)

        return super().patch(request, *args, **kwargs)


class ArticleApprovalAPIView(APIView):

    permission_classes = [IsAuthenticated, IsEditor]

    def get(self, request):

        articles = Article.objects.filter(status=Article.Status.PENDING)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, article_id):

        article = get_object_or_404(Article, id=article_id)
        action = request.data.get("action")

        if action not in ["approve", "reject"]:
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

        article.status = Article.Status.APPROVED if action == "approve" else Article.Status.REJECTED
        article.edited_by = request.user.writer
        article.save()

        return Response({"status": "success"})


class ArticlesEditedAPIView(generics.ListAPIView):

    permission_classes = [IsAuthenticated, IsEditor]
    serializer_class = ArticleSerializer

    def get_queryset(self):

        return Article.objects.filter(
            edited_by=self.request.user.writer,
            status__in=[Article.Status.APPROVED, Article.Status.REJECTED]
        )