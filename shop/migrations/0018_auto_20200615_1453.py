# Generated by Django 3.0.7 on 2020-06-15 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_billingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='countries',
            new_name='country',
        ),
    ]