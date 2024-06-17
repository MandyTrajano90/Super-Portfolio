from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", views.TokenObtainPairView.as_view()),
    path("token/verify/", views.TokenVerifyView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
]
