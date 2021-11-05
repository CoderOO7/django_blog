# Generated by Django 3.2.8 on 2021-11-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
