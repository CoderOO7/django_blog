# Generated by Django 3.2.8 on 2021-10-29 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data_posted',
            new_name='date_posted',
        ),
        migrations.AddField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
