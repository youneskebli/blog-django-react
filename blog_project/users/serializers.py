# serializers.py
from rest_framework import serializers
from blog.models import Writer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = Writer
        fields = ("name", "is_editor", "email", "password")

    def create(self, validated_data):
        user = Writer.objects.create_user(
            name=validated_data["name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
