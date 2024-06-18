from rest_framework import viewsets
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer
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
            user = Profile.objects.get(id=kwargs['pk'])
            user_context = {
                "name": user.name,
                "github": user.github,
                "linkedin": user.linkedin,
                "bio": user.bio,
            }
            return render(request, 'profile_detail.html', user_context)

        return super().retrieve(request, *args, **kwargs)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer