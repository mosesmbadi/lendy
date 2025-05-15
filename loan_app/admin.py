from django.contrib import admin

from .models import Loan, Customer, TransactionDataEndpoint, Repayment

admin.site.register(Loan)
admin.site.register(Customer)
admin.site.register(TransactionDataEndpoint)
admin.site.register(Repayment)
