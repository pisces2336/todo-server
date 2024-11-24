from rest_framework import viewsets

from apps.account.models import User
from apps.account.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
