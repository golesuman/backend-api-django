from django.contrib.auth.models import User
from ecommerce.serializers.user_serializer import RegisterSerializer
from rest_framework import generics, permissions


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
