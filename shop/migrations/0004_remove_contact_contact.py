# Generated by Django 5.0.4 on 2024-05-13 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact',
        ),
    ]
