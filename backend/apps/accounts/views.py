from django.shortcuts import render, redirect
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView,
    UpdateView
    )
# generic - готовые классы с решением для стандартных задач
from .forms import LoginForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth import (
    login,
    authenticate,
    logout
    )
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


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


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('index')   # при успешном запросе перекинет на 'index'
    queryset = User.objects.all()
    model = User

    def test_func(self):    # проверка на совпадение айдишек залогиненного пользователя и айдишки с 'url'
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False


### АНАЛОГ UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView) класса, построенный на функции

# from django.contrib.auth.decorators import login_required
#
# @login_required
# def update_user_profile(request, pk):
#     if request.user.pk != pk:
#         return HttpResponseForbidden()
#     if request.method == "POST":
#         form = UserUpdateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         try:
#             user=User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#         form = UserUpdateForm(instance=user)
#     context = {
#         "form":form
#     }
#     return render(request, 'user_update.html', context)
