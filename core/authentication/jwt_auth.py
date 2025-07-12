from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser


class SimpleUser:
    def __init__(self, user_id):
        self.id = user_id
        self.is_authenticated = True


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get("user_id")
        if not user_id:
            return AnonymousUser()
        return SimpleUser(user_id)
