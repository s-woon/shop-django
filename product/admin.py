from django.contrib import admin
from .models import Product

# Register your models here.



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'stock',
        'available',
        'created',
        'updated',
    ]
    list_editable = [
        'price',
        'stock',
        'available',
    ]
    prepopulated_fields = {
        'slug': (
            'name',
        )
    }
    list_per_page = 20