from django.contrib import admin

from django_orm_samples.models import Currency, Account , Profit, Cost, Transfer, Inventory, CurrencyExchange, Budget, Document, BudgetRecord, BalanceRecord


# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('id', 'name') 
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Profit)
admin.site.register(Cost)
admin.site.register(Transfer)
admin.site.register(Inventory)
admin.site.register(CurrencyExchange)
admin.site.register(Document)
admin.site.register(BudgetRecord)
admin.site.register(BalanceRecord)
