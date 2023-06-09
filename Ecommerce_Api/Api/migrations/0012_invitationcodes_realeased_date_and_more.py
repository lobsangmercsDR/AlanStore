# Generated by Django 4.1.7 on 2023-04-24 15:03

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0011_remove_invitationcodes_realeased_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitationcodes',
            name='realeased_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 1, 15, 3, 36, 983333, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='10t7YUS1KoIYR9z', max_length=15),
        ),
    ]
