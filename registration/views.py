from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {'form': form})

# def signup_page(request):
#     if request.method == 'POST':
#         user_name = request.POST['username']
#         email = request.POST['email']
#         password_1 = request.POST['password1']
#         password_2 = request.POST['password2']
#         if password_1 != password_2:
#             form = True
#         else:
#             my_user = User.objects.create_user(user_name, email, password_1)
#             my_user.save()
#             return redirect('login')
#     return render(request, "registration/signup.html", {'form': form})

def signup_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, "registration/signup.html", {'form': form})

def logout_page(request):
    logout(request)
    return redirect('login')