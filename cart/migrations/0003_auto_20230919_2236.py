# Generated by Django 2.2 on 2023-09-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartlist',
            old_name='class_id',
            new_name='cart_id',
        ),
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
