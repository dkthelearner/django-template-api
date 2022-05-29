# Generated by Django 3.2.13 on 2022-05-29 16:33

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0009_cuisine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Category Name')),
                ('description', models.TextField(blank=True, help_text='Note: e.g describe the about the category.', max_length=300, null=True, verbose_name='Description')),
                ('display_order', models.PositiveSmallIntegerField(blank=True, db_index=True, default=1, help_text='Note: Define the display order of category in consumer phasing application.', null=True, verbose_name='Display Order')),
                ('background_hex_code', colorfield.fields.ColorField(db_index=True, default=False, image_field=None, max_length=18, samples=None, verbose_name='Background Color')),
                ('is_approved', models.BooleanField(db_index=True, default=False, help_text='Note: Mark the category as approved.', verbose_name='Is Approved ?')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_catalog.image')),
            ],
            options={
                'verbose_name': 'Category',
                'db_table': 'category_mst',
            },
        ),
    ]
