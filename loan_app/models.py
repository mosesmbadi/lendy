from django.db import models
import uuid


class Customer(models.Model):
    customer_number = models.CharField(max_length=255)
    reg_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Customer {self.customer_number}"


class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='PENDING')
    loan_score = models.IntegerField(null=True, blank=True)
    limit_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    token = models.CharField(
        max_length=255, null=True, blank=True
    )  # Token from Scoring Engine for subsequent queries
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Loan {self.id} - {self.status} - {self.amount} for {self.customer.customer_number}"


class TransactionDataEndpoint(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    token = models.UUIDField()

    def __str__(self):
        return f"Endpoint {self.name} ({self.url})"
