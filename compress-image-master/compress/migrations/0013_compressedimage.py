# Generated by Django 2.0.2 on 2018-12-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compress', '0012_auto_20181206_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompressedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_compressed_image', models.ImageField(upload_to='generated_images')),
            ],
        ),
    ]
