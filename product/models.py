from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, default='')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    @property
    def get_url(self):
        return reverse(
            'product:product_detail',
            args=[self.slug, self.slug]
        )

    def __str__(self):
        return '{}'.format(self.name)