# Generated by Django 4.0.6 on 2022-08-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_is_active_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='حذف شده'),
        ),
    ]
