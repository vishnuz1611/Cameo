from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterform
from django.contrib.auth import authenticate, get_user_model, login, logout


def signupView(request):
    form = UserRegisterform(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False) # commit = False says not to save the password yet
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)

        if new_user is not None:
            login(request, new_user)
            return redirect('/')
        
    
    return render(request,'accounts/register.html',{'form':form})


def loginView(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    
    return render(request, 'accounts/login.html', {'form':form})


def logoutView(request):
    logout(request)
    return redirect('/')