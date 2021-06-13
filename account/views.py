from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Success')
                else:
                    return HttpResponse('Blocked account!')
            else:
                return HttpResponse('Wrong login or password')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, "Your account has been created. Welcome to SyntaxError —we're happy to have you! 🎉 Please sign-in.")

    user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():

            user_form.save()
            messages.success(request, 'Success update profile')
        else:
            messages.error(request, 'Error update profile')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,
                  'accounts/edit.html',
                  {'user_form': user_form})


@login_required
def dashboard(request):
    return render(request,
                  'accounts/dashboard.html',
                  {'section': 'dashboard'})