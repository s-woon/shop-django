from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from datetime import datetime


class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '장바구니'
        verbose_name_plural = f'{verbose_name} 목록'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name