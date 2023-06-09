# Generated by Django 4.1.7 on 2023-05-18 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0018_alter_invitationcodes_expire_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='registro',
            new_name='createdAt',
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 25, 1, 20, 7, 10371, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='D3MXtIinzNEWWCY', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='rolerequests',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
