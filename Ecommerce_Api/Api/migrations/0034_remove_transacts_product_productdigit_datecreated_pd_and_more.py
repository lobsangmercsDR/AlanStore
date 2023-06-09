# Generated by Django 4.2 on 2023-06-08 20:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0033_alter_invitationcodes_expire_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transacts',
            name='product',
        ),
        migrations.AddField(
            model_name='productdigit',
            name='dateCreated_PD',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transacts',
            name='productDigit',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.productdigit'),
        ),
        migrations.AddField(
            model_name='transacts',
            name='productFisic',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.productfisic'),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 20, 19, 1, 79743, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='223bNppSJwtPrMI', max_length=15),
        ),
    ]
