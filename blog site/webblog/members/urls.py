from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('edit-profile/', views.UserEditProfileView.as_view(), name='edit-profile'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('password/', views.PasswordChangingView.as_view()),
    path('password-success/', views.success, name='password_sucess'),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_profile_page'),
]
