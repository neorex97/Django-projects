# Generated by Django 2.2.3 on 2019-10-31 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='total',
            new_name='sal',
        ),
    ]