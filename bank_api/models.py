from django.db import models
from django.contrib.auth.models import User


class Bank_Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.IntegerField()
    balance = models.DecimalField(default=0, max_digits=20, decimal_places=2)

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


class Transaction(models.Model):
    transaction_id = models.IntegerField()
    account = models.ForeignKey(Bank_Account, on_delete=models.CASCADE)
    from_account_number = models.IntegerField(blank=True, null=True)
    to_account_number = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    # current_balance = models.DecimalField(
    #     max_digits=20, decimal_places=2, blank=True)
    date = models.DateField(auto_now_add=True)
    t_type = models.CharField(max_length=8, choices=[(
        "deposit", "Deposit"), ("withdraw", "Withdraw"), ("sent", "Sent"), ("received", "Received")], default="Null")
    description = models.CharField(max_length=100, blank=True, default='')

    def __str__(self) -> str:
        return f'{self.id}, {self.account.account_number} -> {self.to_account_number}, {self.t_type}'

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'account_number': self.account.account_number,
            "from_account_number": self.from_account_number,
            'to_account_number': self.to_account_number,
            'amount': self.amount,
            'date': self.date,
            't_type': self.t_type,
            'description': self.description
        }
