from django.urls import include, path
from rest_framework import routers

from apps.account.views import UserCreateView, UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("users/", UserCreateView.as_view()),
    path("", include(router.urls)),
]
