# Generated by Django 2.0.2 on 2018-03-24 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palsbet', '0005_visitor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='user',
            new_name='pupil',
        ),
    ]
