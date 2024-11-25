from django.urls import include, path
from rest_framework import routers

from apps.mypage.views import TodoViewSet

router = routers.DefaultRouter()
router.register("todos", TodoViewSet, basename="todo")

urlpatterns = [
    path("", include(router.urls)),
]
