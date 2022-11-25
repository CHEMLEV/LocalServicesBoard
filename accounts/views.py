from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views import generic


from django.conf import settings
User = settings.AUTH_USER_MODEL


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"