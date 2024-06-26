# Generated by Django 5.0.6 on 2024-06-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LiveChat_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]