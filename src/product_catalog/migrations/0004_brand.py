# Generated by Django 3.2.13 on 2022-05-29 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product_catalog', '0003_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(db_index=True, max_length=255, verbose_name='Brand Name')),
                ('is_exclusive',
                 models.BooleanField(db_index=True, default=False, help_text='Note: Mark the brand as exclusive.',
                                     verbose_name='Is Exclusive?')),
                ('is_recognised_brand',
                 models.BooleanField(db_index=True, default=False, help_text='Note: Mark the brand as recognised.',
                                     verbose_name='Is Recognised Brand?')),
                ('is_approved',
                 models.BooleanField(db_index=True, default=False, help_text='Note: Mark the brand as approved.',
                                     verbose_name='Is Approved?')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                               to='product_catalog.image')),
            ],
            options={
                'verbose_name': 'Brand',
                'db_table': 'brand_mst',
            },
        ),
    ]
