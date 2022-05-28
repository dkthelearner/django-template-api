# Generated by Django 3.2.13 on 2022-05-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0002_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notification_name', models.CharField(db_index=True, max_length=255)),
                ('notification_type', models.CharField(choices=[('Email', 'Email'), ('Push', 'Push'), ('Text', 'Text')], db_index=True, max_length=120)),
                ('notification_description', models.TextField()),
                ('notification_type_additional_text', models.TextField()),
                ('is_allowed_to_disabled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Notification',
                'db_table': 'notification_mst',
            },
        ),
        migrations.AlterField(
            model_name='tax',
            name='county_rate',
            field=models.DecimalField(db_index=True, decimal_places=6, max_digits=9, verbose_name='County Tax Rate'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='special_rate',
            field=models.DecimalField(db_index=True, decimal_places=6, max_digits=9, verbose_name='Special Rate'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='state_rate',
            field=models.DecimalField(db_index=True, decimal_places=6, max_digits=9, verbose_name='State Tax Rate'),
        ),
    ]