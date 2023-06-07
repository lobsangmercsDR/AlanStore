# Generated by Django 4.1.7 on 2023-06-07 14:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0032_user_wallet_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 14, 22, 48, 662119, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='x6mzOVmGU0FUmru', max_length=15),
        ),
        migrations.CreateModel(
            name='ProductFisic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProduct', models.CharField(max_length=50)),
                ('image_product', models.ImageField(default=None, upload_to='images/')),
                ('description', models.CharField(default='', max_length=200)),
                ('priceProduct', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateReleased', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('brand', models.CharField(default='', max_length=50)),
                ('aditional_details', models.CharField(default='', max_length=200)),
                ('variants', models.CharField(default='', max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDigit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_PD', models.CharField(max_length=50)),
                ('price_PD', models.DecimalField(decimal_places=2, max_digits=10)),
                ('text_preview_PD', models.CharField(max_length=200)),
                ('quantity_PD', models.IntegerField(default=0)),
                ('subCategory_PD', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.subcategory')),
            ],
        ),
        migrations.AlterField(
            model_name='transacts',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.productfisic'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
