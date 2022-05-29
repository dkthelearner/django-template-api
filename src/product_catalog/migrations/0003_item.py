# Generated by Django 3.2.13 on 2022-05-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product_catalog', '0002_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(db_index=True, help_text='Note: e.g 20 - 20 Nice', max_length=255,
                                               verbose_name='Item Name')),
                ('item_alternate_name', models.TextField(blank=True, db_index=True,
                                                         help_text='Note: e.g Cookies, Biscuits, macaroons, Kukk_kal, Butter Cookies, Kukilu, Kukgalu, Bisketlu, Nut Cookies ',
                                                         max_length=255, null=True,
                                                         verbose_name='Item Alternate Name')),
                ('is_approved',
                 models.BooleanField(db_index=True, default=False, help_text='Note: Mark the item as approved.',
                                     verbose_name='Is Approved?')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Item',
                'db_table': 'item_mst',
            },
        ),
    ]
