from rest_framework import serializers
from .models import Writer, Article


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["id", "is_editor", "name", "email"]


class ArticleSerializer(serializers.ModelSerializer):
    written_by = WriterSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "status", "content", "written_by"]
        read_only_fields = ["written_by"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
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

    def update(self, instance, validated_data):

        if "status" in validated_data:
            raise serializers.ValidationError({"status": "Status cannot be updated"})

        return super().update(instance, validated_data)
