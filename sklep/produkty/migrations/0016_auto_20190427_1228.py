# Generated by Django 2.2 on 2019-04-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0015_auto_20190427_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkty',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
