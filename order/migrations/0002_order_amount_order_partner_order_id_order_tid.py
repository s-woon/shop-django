# Generated by Django 4.0 on 2022-02-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='주문금액'),
        ),
        migrations.AddField(
            model_name='order',
            name='partner_order_id',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='tid',
            field=models.CharField(default='', max_length=250),
        ),
    ]