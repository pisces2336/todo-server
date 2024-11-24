from django.urls import include, path
from rest_framework import routers

from apps.account.views import UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
