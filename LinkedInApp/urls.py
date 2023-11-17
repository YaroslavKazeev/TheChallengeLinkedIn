from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('members/', views.members_view, name='members'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path("", include("django.contrib.auth.urls")),
]