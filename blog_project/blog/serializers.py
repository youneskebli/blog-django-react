from rest_framework import serializers
from .models import Writer, Article


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["id", "is_editor"]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "status", "content", "written_by"]
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        written_by = representation.get("written_by", {})
        if written_by:
            representation["written_by"] = {
                "id": written_by["id"],
                "email": written_by["email"],
                "name": written_by["name"],
            }

        return representation


class ArticleDetailSerializer(serializers.ModelSerializer):
    written_by = WriterSerializer(read_only=True)
    edited_by = WriterSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "content",
            "status",
            "written_by",
            "edited_by",
            "created_at",
        ]
        read_only_fields = ["status", "written_by", "created_at", "edited_by"]
