# Generated by Django 3.1.1 on 2020-09-08 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['technologies']},
        ),
    ]
