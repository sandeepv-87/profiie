# Generated by Django 4.2 on 2023-05-05 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='number',
            new_name='phone',
        ),
    ]
