# Generated by Django 5.0.6 on 2024-07-02 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LiveChat_app', '0017_chat_file_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat_msg',
            old_name='files_id',
            new_name='chat_file_id',
        ),
    ]
