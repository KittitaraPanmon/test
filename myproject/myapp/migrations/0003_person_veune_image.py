# Generated by Django 4.2.2 on 2023-06-19 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_person_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='veune_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]