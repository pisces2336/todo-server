from rest_framework import serializers

from apps.account.serializers import UserSerializer
from apps.mypage.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()
    user = UserSerializer(required=False)

    class Meta:
        model = Todo
        fields = ("id", "title", "description", "due", "user_id", "user")
