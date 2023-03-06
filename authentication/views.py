from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import LoginForm
from .forms import UserRegistrationForm

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, template_name="authentication/login_form.html", context=context)

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            login(request, user)
            return HttpResponseRedirect("/")
        context = {"form": form}

        return render(request, template_name="authentication/login_form.html", context=context)


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return redirect("home")
    else:
        user_form = UserRegistrationForm()
    return render(request, "authentication/register.html", {"user_form": user_form})


def logout_user(request):
    logout(request)
    return redirect("main_page")
