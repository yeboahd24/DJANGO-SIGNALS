from django.db import models
from orders.models import Order
class Sale(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.amount)
    