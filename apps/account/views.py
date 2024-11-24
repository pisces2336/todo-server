from rest_framework import response, settings, status, views, viewsets

from apps.account.models import User
from apps.account.serializers import UserSerializer


class UserCreateView(views.APIView):
    authentication_classes = []

    # ユーザー作成時には権限を要しないためエンドポイントを分ける
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {"Location": str(data[settings.api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
