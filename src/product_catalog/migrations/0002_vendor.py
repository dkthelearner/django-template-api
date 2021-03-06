# Generated by Django 3.2.13 on 2022-05-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('qb_id', models.CharField(db_index=True, max_length=30)),
                ('vendor_company_name', models.CharField(db_index=True, max_length=255)),
                ('vendor_address', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_city', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor_zip_pin_code', models.CharField(blank=True, max_length=15, null=True)),
                ('vendor_country', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Vendor',
                'db_table': 'vendors',
            },
        ),
    ]
