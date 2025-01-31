from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ProjectViewSet, CertifyingInstitutionViewSet, CertificateViewSet


router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'certifying-institutions', CertifyingInstitutionViewSet)
router.register(r'certificates', CertificateViewSet)