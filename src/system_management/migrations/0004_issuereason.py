# Generated by Django 3.2.13 on 2022-05-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0003_auto_20220528_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueReason',
            fields=[
                ('issue_reason_id', models.AutoField(primary_key=True, serialize=False)),
                ('reason_label', models.CharField(db_index=True, max_length=255)),
                ('reason_type', models.CharField(choices=[('Delivery/Pickup', 'Delivery/Pickup'), ('Product Level', 'Product Level')], db_index=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'IssueReason',
                'db_table': 'issue_reason_mst',
            },
        ),
    ]