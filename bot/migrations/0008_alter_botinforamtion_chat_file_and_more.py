# Generated by Django 4.2.14 on 2024-08-15 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bot', '0007_chatdescription_alter_botinforamtion_botdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botinforamtion',
            name='chat_file',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='botinforamtion',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='botinforamtion',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]