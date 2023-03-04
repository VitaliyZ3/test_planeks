from typing import ContextManager
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.views import View

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, template_name='authentication/login_form.html', context=context)
    
    def post(self, request):
        
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/admin')
        context = {'form': form}
       
        return render(request, template_name='authentication/login_form.html', context=context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'user_form': user_form})