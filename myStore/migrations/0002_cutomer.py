# Generated by Django 5.1 on 2024-09-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cutomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
