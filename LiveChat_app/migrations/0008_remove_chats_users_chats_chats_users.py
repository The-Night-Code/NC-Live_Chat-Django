# Generated by Django 5.0.6 on 2024-06-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LiveChat_app', '0007_chats_grp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='users',
        ),
        migrations.AddField(
            model_name='chats',
            name='chats_users',
            field=models.TextField(blank=True),
        ),
    ]
