from django.urls import path, include
from .views import RegisterView, GoogleLogin

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('social/google/', GoogleLogin.as_view(), name='google_login'),
    path('', include('dj_rest_auth.urls')),
]