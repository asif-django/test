# Generated by Django 3.0.7 on 2020-09-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_app', '0003_auto_20200907_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale_items',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='sale_items',
            name='total_vat',
        ),
        migrations.AddField(
            model_name='sale',
            name='net_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Net_Amount'),
        ),
        migrations.AddField(
            model_name='sale',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mobile Number'),
        ),
        migrations.AddField(
            model_name='sale',
            name='total_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Total_Amount'),
        ),
        migrations.AddField(
            model_name='sale',
            name='total_vat',
            field=models.FloatField(blank=True, null=True, verbose_name='GST Amount'),
        ),
    ]
