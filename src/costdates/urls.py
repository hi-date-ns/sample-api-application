from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CostDateViewSet

router = DefaultRouter()
router.register("", CostDateViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
