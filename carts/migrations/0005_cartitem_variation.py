# Generated by Django 4.2.5 on 2023-10-11 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_is_available_variation_is_active'),
        ('carts', '0004_alter_cartitem_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]