# Generated by Django 2.0.4 on 2018-04-18 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Sender',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='user',
            new_name='sender',
        ),
    ]
