# Generated by Django 3.1.5 on 2021-03-09 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('split', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoaderReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('format', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='avfile',
            name='avfile',
            field=models.FileField(upload_to='uploads'),
        ),
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=25)),
                ('filename', models.CharField(max_length=250)),
                ('filetype', models.CharField(max_length=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]