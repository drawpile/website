# Generated by Django 3.2.25 on 2024-11-04 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpauth', '0010_username_dpauth_user_normali_c07dcb_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorWordList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_type', models.CharField(choices=[('wordlist', 'wordlist - words not allowed in SFM sessions'), ('nsfm_wordlist', 'nsfm_wordlist - words not even allowed in NSFM sessions'), ('allowlist', 'allowlist - words to ignore (verbatim)'), ('silent_wordlist', 'silent_wordlist - words that trigger a silent alert')], max_length=16, unique=True)),
                ('words', models.TextField(help_text='Check drawpile-monitor documentation for the format.')),
            ],
        ),
    ]