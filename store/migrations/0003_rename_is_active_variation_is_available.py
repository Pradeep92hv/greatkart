# Generated by Django 4.2.5 on 2023-10-03 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='is_active',
            new_name='is_available',
        ),
    ]