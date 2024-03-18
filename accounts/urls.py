from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.SignInView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("settings/", views.AccountSettingsView.as_view(), name="account_settings"),
]
