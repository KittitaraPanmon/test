# Generated by Django 4.2.2 on 2023-06-19 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
