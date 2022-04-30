from django.shortcuts import render, redirect
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView
    )
# generic - готовые классы с решением для стандартных задач
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth import (
    login,
    authenticate,
    logout
    )
from django.http import HttpResponse
from django.urls import reverse_lazy

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого юзера не существует")


class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('register_done')


class RegisterDoneView(TemplateView):
    template_name = 'register_done.html'


def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
