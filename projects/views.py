from rest_framework import viewsets
from .models import Profile, Project, CertifyingInstitution, Certificate
from .serializers import ProfileSerializer, ProjectSerializer, CertifyingInstitutionSerializer, CertificateSerializer   
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            user = self.get_object()
            user_context = {
                'name': user.name,
                'github': user.github,
                'linkedin': user.linkedin,
                'bio': user.bio,
                'projects': user.projects.all(),
                'certificates': user.certificates.all()
            }
            return render(request, 'profile_detail.html', user_context)

        return super().retrieve(request, *args, **kwargs)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
    permission_classes = [IsAuthenticated]

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]