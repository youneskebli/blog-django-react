from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from blog.models import Writer
from .mixins import TokenMixin


class RegisterView(generics.CreateAPIView):
    queryset = Writer.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = Writer.objects.get(email=response.data["email"])

        return Response(
            {
                "user_id": user.pk,
                "email": user.email,
                "name": user.name,
                "is_editor": user.is_editor,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(TokenMixin,APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user is not None:
            tokens = self.get_tokens_for_user(user)
            return Response(
                {
                    "access_token": tokens["access_token"],
                    "refresh_token": tokens["refresh_token"],
                    "user_id": user.pk,
                    "email": user.email,
                    "name": user.writer.name,
                    "is_editor": user.writer.is_editor,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )
