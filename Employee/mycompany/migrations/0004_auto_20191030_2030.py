# Generated by Django 2.2.3 on 2019-10-30 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0003_auto_20191030_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='desig',
            new_name='designn',
        ),
    ]
