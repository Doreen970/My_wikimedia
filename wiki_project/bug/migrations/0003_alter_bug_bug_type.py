# Generated by Django 4.1.7 on 2023-10-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_alter_bug_bug_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='bug_type',
            field=models.CharField(choices=[('error', 'error'), ('new feature', 'new feature'), ('malware attack', 'malware attack'), ('Test Bug', 'Test Bug')], max_length=100),
        ),
    ]
