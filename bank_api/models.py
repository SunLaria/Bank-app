from django.db import models
from django.contrib.auth.models import User
import random


class Bank_Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.IntegerField()
    balance = models.DecimalField(default=0, max_digits=20, decimal_places=3)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'account_number': self.account_number,
            'balance': self.balance
        }

    def __repr__(self) -> str:
        return f'{self.id, self.user.username, self.account_number, self.balance}'

    def __str__(self) -> str:
        return f'{self.account_number}'


class Transition(models.Model):
    account = models.ForeignKey(Bank_Account, on_delete=models.CASCADE)
    to_account_number = models.IntegerField(blank=True)
    amount = models.DecimalField(default=0, max_digits=20, decimal_places=3)
    date = models.DateTimeField(auto_now_add=True)
    t_type = models.CharField(max_length=8, choices=[(
        "deposit", "Deposit"), ("withdraw", "Withdraw"), ("transfer", "Transfer")], default="Null")
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.id}, {self.account.account_number} -> {self.to_account_number}'
