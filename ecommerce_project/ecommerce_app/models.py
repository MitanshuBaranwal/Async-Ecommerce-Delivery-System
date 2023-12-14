from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, default="Pending")
    quantity = models.PositiveIntegerField()
    product_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order ID: {self.order_id}, Product: {self.product_name}, Quantity: {self.quantity}"