# Generated by Django 3.0.7 on 2020-06-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200604_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
