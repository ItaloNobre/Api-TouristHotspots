# Generated by Django 4.1.4 on 2022-12-16 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('core', '0004_touristhotspot_attractions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristhotspot',
            name='attractions',
            field=models.ManyToManyField(to='comments.comment'),
        ),
    ]
