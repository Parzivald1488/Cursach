# Generated by Django 4.1.4 on 2022-12-10 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='subjects',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subjects',
        ),
    ]
