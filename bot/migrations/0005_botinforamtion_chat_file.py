# Generated by Django 5.0.6 on 2024-08-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_botinforamtion_delete_bot_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='botinforamtion',
            name='chat_file',
            field=models.FileField(blank=True, null=True, upload_to='media/chats'),
        ),
    ]
