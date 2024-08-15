# Generated by Django 5.0.6 on 2024-08-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_botinforamtion_botdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media\\images')),
                ('chat_file', models.FileField(blank=True, null=True, upload_to='media/chats')),
                ('botdescription', models.CharField(default='My favourite person', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='botinforamtion',
            name='botdescription',
            field=models.CharField(blank=True, default='my favourite person', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='botinforamtion',
            name='name',
            field=models.CharField(blank='False', max_length=255),
        ),
    ]