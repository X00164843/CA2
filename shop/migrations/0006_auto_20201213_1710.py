# Generated by Django 3.1.3 on 2020-12-13 17:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_type', models.ManyToManyField(to='shop.Product')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
