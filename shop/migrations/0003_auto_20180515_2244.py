# Generated by Django 2.0.3 on 2018-05-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180515_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара'),
        ),
    ]
