# Generated by Django 3.0.7 on 2020-09-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_app', '0004_auto_20200907_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Total_Amountt'),
        ),
    ]
