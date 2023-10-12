# Generated by Django 3.2.19 on 2023-10-12 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dpauth', '0003_ban_baniprange_bansystemidentifier_banuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('comment', models.TextField(help_text='Verification reason, provide links to socials/galleries if possible')),
                ('exempt_from_bans', models.BooleanField(default=False, help_text='System ID, user and session bans still hold regardless', verbose_name='Exempt from IP bans')),
            ],
        ),
    ]
