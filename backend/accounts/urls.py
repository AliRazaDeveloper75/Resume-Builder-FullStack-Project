from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('profile/', views.user_profile_view, name='profile'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
]