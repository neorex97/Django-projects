# Generated by Django 2.2.3 on 2019-10-31 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cat',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nam',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pri',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='spe',
            new_name='spec',
        ),
    ]