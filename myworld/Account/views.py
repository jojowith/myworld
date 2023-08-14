from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from . forms import SignUpForm, UserCreationForm
from django.contrib import messages


# Create your views here.


def account_signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('post:list')
        else:
            messages.success(request, ("帳號或密碼錯誤!"))
    return render(request, 'account/SigninForm.html')


def account_signup_view(request):
    if request.user.is_anonymous:
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            form.save()
            new_user = authenticate(first_name=first_name, username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("accounts:signin")
    else:
        return redirect("accounts:signup")

    form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'account/SignupForm.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')