# Generated by Django 4.1.7 on 2023-07-05 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0073_reporttransacts_noreporte_reporttransacts_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacts',
            name='company',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transacts',
            name='noSeguimiento',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 13, 30, 33, 57439, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='gFy5I5fdob5nhIT', max_length=15),
        ),
    ]
