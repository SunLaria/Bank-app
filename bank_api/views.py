from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, Bank_Account, Transaction
import json
from django.contrib.auth.decorators import login_required
from .functions import random_transaction_id


@login_required(login_url='/login/')
def withdraw(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        #  check if amount is valid
        if request_json.get("amount", 0) > 0:
            # check if account have enough money to withdraw
            if Bank_Account.objects.get(user=request.user).balance >= request_json["amount"]:
                # decreasing account balance
                Bank_Account.objects.get(
                    user=request.user).balance -= request_json["amount"]
                # create Transaction record for user
                Transaction.objects.create(transaction_id=random_transaction_id(),
                                           account=request.user,
                                           amount=request_json["amount"],
                                           current_balance=request.user.balance,
                                           t_type="withdraw",
                                           description=request_json["description"])
                return "Withdrawal Successfully"
            else:
                return "Insufficient Balance"
        else:
            return "Invalid Amount"
    else:
        return "POST Request Only!"


@login_required(login_url='/login/')
def deposit(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        #  check if amount is valid
        if request_json.get("amount", 0) > 0:
            # Increase Account balance
            Bank_Account.objects.get(
                user=request.user).balance += request_json["amount"]
            #  create Transaction record for user
            Transaction.objects.create(transaction_id=random_transaction_id(),
                                       account=request.user,
                                       amount=request_json["amount"],
                                       current_balance=request.user.balance,
                                       t_type="deposit",
                                       description=request_json["description"])
            return "Deposit Successfully"
        else:
            return "Invalid Amount"
    else:
        return "POST Request Only!"


@login_required(login_url='/login/')
def transfer(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        #  check if amount is valid
        if request_json.get("amount", 0) > 0:
            #  check if account have enough money to transfer
            if Bank_Account.objects.get(user=request.user).balance >= request_json["amount"]:
                #  check if account exist
                if Bank_Account.objects.filter(account_number=request_json["to_account_number"]).exists():
                    #  check if receiver account is not sender account
                    if request.user.account_number != request_json["to_account_number"]:
                        # decrease sender money balance
                        Bank_Account.objects.get(
                            user=request.user).balance -= request_json["amount"]
                        # increase receiver money balance
                        Bank_Account.objects.get(
                            account_number=request_json["to_account_number"]).balance += request_json["amount"]
                        # create Transaction record for sender and receiver
                        transaction_id = random_transaction_id()
                        Transaction.objects.create(transaction_id=transaction_id,
                                                   account=request.user,
                                                   to_account_number=request_json["to_account_number"],
                                                   amount=request_json["amount"],
                                                   t_type="sent",
                                                   description=request_json["description"])
                        Transaction.objects.create(transaction_id=transaction_id,
                                                   account=Bank_Account.objects.get(
                                                       account_number=request_json["to_account_number"]),
                                                   from_account_number=request.user.bank_account.account_number,
                                                   amount=request_json["amount"],
                                                   t_type="received",
                                                   description=request_json["description"])

                        return "Transfer Successfully"
                    else:
                        return "Sender Account and Receiver Account Cannot be Same"
                else:
                    return "Receiver Account Does Not Exist"
            else:
                return "Insufficient Balance"
        else:
            return "Invalid Amount"
    else:
        return "POST Request Only!"
