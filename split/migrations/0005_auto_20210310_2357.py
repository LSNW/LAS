# Generated by Django 3.1.5 on 2021-03-11 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('split', '0004_auto_20210310_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerecord',
            old_name='author',
            new_name='user',
        ),
    ]
