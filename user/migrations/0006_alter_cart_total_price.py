# Generated by Django 4.1.4 on 2023-03-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_cart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=5, max_digits=50),
        ),
    ]