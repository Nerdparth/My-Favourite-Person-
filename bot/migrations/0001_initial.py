# Generated by Django 5.0.6 on 2024-08-06 07:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bot_information',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='media\\images')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]