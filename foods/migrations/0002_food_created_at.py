# Generated by Django 5.0.7 on 2024-08-02 15:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
