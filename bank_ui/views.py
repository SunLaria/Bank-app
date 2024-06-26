from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from bank_api.models import Bank_Account, Transaction
from .functions import random_bank_number


# Create your views here.


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated != True:
            login_form = LoginForm()
            return render(request, 'login.html', {'login_form': login_form})
        else:
            return redirect('home')
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'].lower(), password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')


def logout_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')


def register_view(request):
    if request.method == 'GET':
        register_form = UserCreationForm()
        return render(request, 'register.html', {'register_form': register_form})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            Bank_Account.objects.create(
                user=user, account_number=random_bank_number(), balance=0)
            # login(request, user)
            messages.success(request, 'You Have Signed Up Successfully.')
            return redirect('register')
        else:
            messages.error(request, "Registration Failed")
            return redirect('register')


@login_required(login_url="/login/")
def home(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'home.html')
        else:
            return redirect('login')


@ login_required(login_url="/login/")
def balance(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'balance.html')
        else:
            return redirect('login')


@ login_required(login_url="/login/")
def deposit(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'deposit.html')
        else:
            return redirect('login')


@ login_required(login_url="/login/")
def withdraw(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'withdraw.html')
        else:
            return redirect('login')


@ login_required(login_url="/login/")
def transfer(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'transfer.html')
        else:
            return redirect('login')
