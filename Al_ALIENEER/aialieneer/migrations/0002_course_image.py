# Generated by Django 3.2.1 on 2021-05-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aialieneer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='aialieneer/images'),
        ),
    ]
