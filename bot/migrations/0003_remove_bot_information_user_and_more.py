# Generated by Django 5.0.6 on 2024-08-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_remove_bot_information_image_bot_information_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot_information',
            name='user',
        ),
        migrations.AlterField(
            model_name='bot_information',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='bot_information',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
