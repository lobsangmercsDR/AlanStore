# Generated by Django 4.2 on 2023-04-12 01:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
