# Generated by Django 3.0.7 on 2020-11-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_app', '0003_auto_20201103_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='free_quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Free Quantity'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='sale_quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Sale Quantity'),
        ),
    ]
