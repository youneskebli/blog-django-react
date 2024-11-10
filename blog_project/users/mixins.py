from rest_framework_simplejwt.tokens import RefreshToken

class TokenMixin:
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }