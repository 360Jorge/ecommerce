# Generated by Django 3.2.2 on 2021-05-26 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_totaprice_order_totalprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='padiAt',
            new_name='paidAt',
        ),
    ]
