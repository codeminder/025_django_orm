# Generated by Django 3.2.13 on 2022-05-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_orm_samples', '0004_auto_20220424_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost',
            name='posted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currency',
            name='course',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='currencyexchange',
            name='posted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inventory',
            name='posted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profit',
            name='posted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transfer',
            name='posted',
            field=models.BooleanField(default=False),
        ),
    ]