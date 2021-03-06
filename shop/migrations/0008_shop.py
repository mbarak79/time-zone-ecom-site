# Generated by Django 3.0.7 on 2020-06-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200613_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('item_image', models.ImageField(upload_to='Shop/')),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
