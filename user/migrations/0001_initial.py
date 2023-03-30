# Generated by Django 4.1.4 on 2023-03-10 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0004_rename_image_products_thumbnail_album'),
        ('home', '0005_seller_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.products')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.variant')),
            ],
        ),
    ]
