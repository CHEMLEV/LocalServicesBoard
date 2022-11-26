
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateUserForm

from django.conf import settings
User = settings.AUTH_USER_MODEL


class SignUpView(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"