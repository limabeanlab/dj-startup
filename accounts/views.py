from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from django.urls import reverse

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # Process the form data here (e.g., save user, send confirmation email)
        return super().form_valid(form)

    # redirect logged in user to dashboard
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("crm:dashboard")
        else:
            return super().get(request)


class SignInView(LoginView):
    success_url = reverse_lazy("crm:dashboard")
    template_name = "registration/login.html"

    # redirect logged in user to dashboard
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("crm:dashboard")
        else:
            return super().get(request)


# AllAuth LoginView (LinkedIn, Google, etc.)
# NOT SURE THIS IS WORKING
# class SignInAllAuthView(AllAuthLoginView):
#     template = "socialaccount/login.html"

#     def dispatch(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect(
#                 reverse("dashboard")
#             )  # Replace 'dashboard' with your actual dashboard URL name
#         return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"

    def get(self, request):
        user = request.user
        return render(request, "registration/profile.html", {"user": user})


class AccountSettingsView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("account_settings")
    template_name = "registration/account_settings.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
