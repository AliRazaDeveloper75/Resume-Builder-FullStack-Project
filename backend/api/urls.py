from django.urls import path
from . import views

urlpatterns = [
    path('protected/', views.protected_view, name='protected'),
    path('public/', views.public_view, name='public'),
]