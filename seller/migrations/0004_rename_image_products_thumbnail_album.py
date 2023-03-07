# Generated by Django 4.1.4 on 2023-03-01 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_remove_variant_sku'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='image',
            new_name='thumbnail',
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.products')),
            ],
        ),
    ]
