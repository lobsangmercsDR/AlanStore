# Generated by Django 4.1.7 on 2023-06-24 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0066_productdigit_comisioncheck_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdigit',
            name='no_solicitud',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 1, 19, 50, 39, 362110, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='EDUjSdm5mvjcflB', max_length=15),
        ),
    ]