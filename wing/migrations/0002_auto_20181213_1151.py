# Generated by Django 2.1.4 on 2018-12-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extras',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='vegetable',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
