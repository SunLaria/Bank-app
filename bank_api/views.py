from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Bank_Account, Transaction
import json
from django.contrib.auth.decorators import login_required
from .functions import random_transaction_id


@login_required(login_url='/login/')
def withdraw(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        if request_json.get("amount", 0) > 0:
            user_bank_account = request.user.bank_account
            if user_bank_account.balance >= request_json["amount"]:
                user_bank_account.balance -= request_json["amount"]
                user_bank_account.save()
                Transaction.objects.create(transaction_id=random_transaction_id(),
                                           account=request.user.bank_account,
                                           amount=request_json["amount"],
                                           t_type="withdraw",
                                           description=request_json["description"])
                return JsonResponse({"result": "Withdrawal Successfully"})
            else:
                return JsonResponse({"result": "Insufficient Balance"})

        else:
            return JsonResponse({"result": "Invalid Amount"})


@login_required(login_url='/login/')
def deposit(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        if request_json.get("amount", 0) > 0:
            user_bank_account = request.user.bank_account
            user_bank_account.balance += request_json["amount"]
            user_bank_account.save()
            Transaction.objects.create(transaction_id=random_transaction_id(),
                                       account=request.user.bank_account,
                                       amount=request_json["amount"],
                                       t_type="deposit",
                                       description=request_json["description"])
            return JsonResponse({"result": "Deposit Successfully"})
        else:
            return JsonResponse({"result": "Invalid Amount"})


@login_required(login_url='/login/')
def transfer(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        if request_json["amount"] > 0:
            user_bank_account = request.user.bank_account
            if user_bank_account.balance >= request_json["amount"]:
                if Bank_Account.objects.filter(account_number=request_json["to_account_number"]).exists():
                    if request.user.bank_account.account_number != int(request_json["to_account_number"]):
                        user_bank_account.balance -= request_json["amount"]
                        user_bank_account.save()
                        receiver_bank_account = Bank_Account.objects.get(
                            account_number=request_json["to_account_number"])
                        receiver_bank_account.balance += request_json["amount"]
                        receiver_bank_account.save()
                        transaction_id = random_transaction_id()
                        Transaction.objects.create(transaction_id=transaction_id,
                                                   account=request.user.bank_account,
                                                   from_account_number=request.user.bank_account.account_number,
                                                   to_account_number=request_json["to_account_number"],
                                                   amount=request_json["amount"],
                                                   t_type="sent",
                                                   description=request_json["description"])
                        Transaction.objects.create(transaction_id=transaction_id,
                                                   account=Bank_Account.objects.get(
                                                       account_number=request_json["to_account_number"]),
                                                   from_account_number=request.user.bank_account.account_number,
                                                   to_account_number=request_json["to_account_number"],
                                                   amount=request_json["amount"],
                                                   t_type="received",
                                                   description=request_json["description"])

                        return JsonResponse({"result": "Transfer Successfully"})
                    else:
                        return JsonResponse({"result": "Sender Account and Receiver Account Cannot be Same"})
                else:
                    return JsonResponse({"result": "Receiver Account Does Not Exist"})
            else:
                return JsonResponse({"result": "Insufficient Balance"})
        else:
            return JsonResponse({"result": "Invalid Amount"})
