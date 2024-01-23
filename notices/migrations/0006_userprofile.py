# Generated by Django 4.2.4 on 2024-01-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0005_remove_notice_attachments_delete_attachment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
