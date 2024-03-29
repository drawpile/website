# Generated by Django 3.2.19 on 2024-03-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpusers', '0002_pendingdeletion'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_type', models.IntegerField(choices=[(1, 'Signup'), (2, 'Password Reset'), (3, 'Email Change')], help_text='What kind of email this was')),
                ('raw_address', models.CharField(help_text='Verbatim email address', max_length=255)),
                ('normalized_address', models.CharField(help_text='Normalized email address for querying', max_length=255)),
                ('sent_at', models.DateTimeField(auto_now_add=True, help_text='When the email was sent')),
            ],
        ),
        migrations.AddIndex(
            model_name='sentemail',
            index=models.Index(fields=['normalized_address'], name='dpusers_sen_normali_cbe752_idx'),
        ),
        migrations.AddIndex(
            model_name='sentemail',
            index=models.Index(fields=['sent_at'], name='dpusers_sen_sent_at_566323_idx'),
        ),
    ]
