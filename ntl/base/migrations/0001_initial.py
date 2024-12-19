# Generated by Django 5.1.4 on 2024-12-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=25)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
