# Generated by Django 2.0.2 on 2018-12-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compress', '0009_auto_20181203_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(height_field='100', upload_to='images', width_field='100'),
        ),
    ]
