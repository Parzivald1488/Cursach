# Generated by Django 4.1.4 on 2022-12-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Название')),
                ('start', models.TimeField(verbose_name='Начало')),
                ('end', models.TimeField(verbose_name='Конец')),
            ],
        ),
    ]
