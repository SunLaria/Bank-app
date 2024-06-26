from django.contrib import admin


from .models import Bank_Account, Transaction

admin.site.register(Bank_Account)
admin.site.register(Transaction)
