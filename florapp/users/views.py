from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic  import FormView

from users.forms import SignUpForm

class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'

class SignUpView(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        "Safe form data"
        form.save()
        return super().form_valid(form)
