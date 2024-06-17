from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ProjectViewSet


router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)