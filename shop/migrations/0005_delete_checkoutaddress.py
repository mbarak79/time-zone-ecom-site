# Generated by Django 3.0.7 on 2020-06-12 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_checkoutaddress'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckoutAddress',
        ),
    ]