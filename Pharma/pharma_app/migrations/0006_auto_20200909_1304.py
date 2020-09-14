# Generated by Django 3.0.7 on 2020-09-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_app', '0005_auto_20200907_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='bill_no',
            field=models.CharField(blank=True, choices=[('Ramnagar', 'Ramnagar'), ('B', 'ABCD'), ('C', 'XYZ')], max_length=50, null=True, verbose_name='Store'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='received_store',
            field=models.CharField(blank=True, choices=[('Ramnagar', 'Ramnagar'), ('B', 'ABCD'), ('C', 'XYZ')], max_length=50, null=True, verbose_name='Received Store'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Card', 'Card'), ('UPI', 'UPI'), ('Others', 'Others')], max_length=50, null=True, verbose_name='Bill_No'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='store',
            field=models.CharField(blank=True, choices=[('Ramnagar', 'Ramnagar'), ('B', 'ABCD'), ('C', 'XYZ')], max_length=50, null=True, verbose_name='Store'),
        ),
    ]