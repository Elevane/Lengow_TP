# Generated by Django 2.2.1 on 2019-05-26 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='idFlux',
            new_name='cancel',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='lengow',
            new_name='new',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='marketplace',
            new_name='processing',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='shipped',
        ),
    ]
