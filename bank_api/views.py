from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, Bank_Account, Transition
import json
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/login/')
def user_data(request):
    if request.method == 'GET':
        try:
            return json.dumps(Bank_Account.objects.get(user=request.user).to_dict())
        except:
            return "No Bank Account Found"
    else:
        return "GET Request Only!"


# @login_required(login_url='/login/')
def withdraw(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        if request_json.get("amount", 0) > 0:
            if Bank_Account.objects.get(user=request.user).balance >= request_json["amount"]:
                Bank_Account.objects.get(
                    user=request.user).balance -= request_json["amount"]
                return "Withdrawal Successfully"
            else:
                return "Insufficient Balance"
        else:
            return "Invalid Amount"
    else:
        return "POST Request Only!"


# @login_required(login_url='/login/')


def deposit(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        if request_json.get("amount", 0) > 0:
            Bank_Account.objects.get(
                user=request.user).balance += request_json["amount"]
            return "Deposit Successfully"
        else:
            return "Invalid Amount"
    else:
        return "POST Request Only!"


# @login_required(login_url='/login/')
def transfer(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        if request_json.get("amount", 0) > 0:
            if Bank_Account.objects.get(user=request.user).balance >= request_json["amount"]:
                # action
                return "Withdrawal Successfully"


# @login_required(login_url='/login/')
def accept_transfer(request):
    return HttpResponse("accept-sent!")
