# Generated by Django 4.2.4 on 2023-08-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/')),
            ],
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='timestamp',
            new_name='posted_date',
        ),
        migrations.AddField(
            model_name='notice',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='notices.attachment'),
        ),
    ]
