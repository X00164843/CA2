# Generated by Django 3.1.3 on 2020-12-13 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20201213_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'product type', 'verbose_name_plural': 'product types'},
        ),
    ]