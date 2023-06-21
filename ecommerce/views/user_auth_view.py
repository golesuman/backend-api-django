from django.contrib.auth.models import User
from rest_framework import generics, permissions, response, views

from ecommerce.serializers.user_serializer import (
    RegisterSerializer,
    UserProfileSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class UserProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        user = User.objects.filter(id=user.id).first()
        serializer = UserProfileSerializer(user)
        return response.Response(serializer.data)
