# Generated by Django 4.1.4 on 2022-12-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('subjects', models.ManyToManyField(blank=True, to='app.subject')),
            ],
        ),
    ]
