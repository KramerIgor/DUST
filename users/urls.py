from django.urls import path
from .views import UserRegistration, UserLogin, ProfileView

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-create'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]