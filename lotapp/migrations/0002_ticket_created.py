# Generated by Django 5.0.4 on 2024-04-19 17:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
