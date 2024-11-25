from rest_framework import viewsets

from apps.mypage.models import Todo
from apps.mypage.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = (
            Todo.objects.select_related("user").filter(user=user).order_by("created_at")
        )
        return queryset
