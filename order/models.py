from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    partner_order_id = models.CharField(max_length=250, default='')
    tid = models.CharField(max_length=250, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='주문시간')
    amount = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='주문금액', default=0)

    class Meta:
        db_table = 'consumer_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'