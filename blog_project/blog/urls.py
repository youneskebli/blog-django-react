from django.urls import path
from .views import (
    DashboardAPIView,
    ArticleCreateAPIView,
    ArticleDetailAPIView,
    ArticleApprovalAPIView,
    ArticlesEditedAPIView,
)

urlpatterns = [
    path("", DashboardAPIView.as_view(), name="dashboard"),
    path("article/create/",
         ArticleCreateAPIView.as_view(),
         name="article-create"),
    path("article/<int:id>/",
         ArticleDetailAPIView.as_view(),
         name="article-detail"),
    path(
        "articles/approval/",
        ArticleApprovalAPIView.as_view(),
        name="article-approval-list",
    ),
    path(
        "articles/approval/<int:article_id>/",
        ArticleApprovalAPIView.as_view(),
        name="article-approval-action",
    ),
    path(
        "articles/articles-edited/",
        ArticlesEditedAPIView.as_view(),
        name="articles-edited",
    ),
]
