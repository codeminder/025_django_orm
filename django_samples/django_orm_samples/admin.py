from django.contrib import admin

from django_orm_samples.models import Currency, Account , Profit, Cost, Transfer, Inventory, CurrencyExchange, Budget, Document, BudgetRecord, BalanceRecord


# Register your models here.

admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Budget)
admin.site.register(Profit)
admin.site.register(Cost)
admin.site.register(Transfer)
admin.site.register(Inventory)
admin.site.register(CurrencyExchange)
admin.site.register(Document)
admin.site.register(BudgetRecord)
admin.site.register(BalanceRecord)
