# Generated by Django 3.1.3 on 2023-04-06 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20230406_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='correct',
            new_name='is_correct',
        ),
    ]
