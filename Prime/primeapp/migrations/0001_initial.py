# Generated by Django 2.2.3 on 2019-11-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxn', models.ImageField(upload_to='')),
                ('minn', models.ImageField(upload_to='')),
            ],
        ),
    ]