# Generated by Django 3.2.19 on 2024-03-19 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatepages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[-.\\w]+$')])),
                ('permission', models.CharField(blank=True, max_length=512)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
