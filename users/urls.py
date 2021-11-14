from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.auth_register, name='users-register'),
    path('login/', views.auth_login, name='users-login'),
    path('logout/', views.auth_logout, name='users-logout'),
    path('profile/',views.profile, name='users-profile')
]
