import random
from bank_api.models import Bank_Account


def random_bank_number():
    while True:
        random_bank_number = random.randint(1000000000, 9999999999)
        if Bank_Account.objects.filter(account_number=random_bank_number).exists() == False:
            return random_bank_number
