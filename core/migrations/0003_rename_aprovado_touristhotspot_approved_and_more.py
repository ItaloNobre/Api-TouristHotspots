# Generated by Django 4.1.4 on 2022-12-16 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_touristhotspot_delete_pontoturistico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='touristhotspot',
            old_name='aprovado',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='touristhotspot',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='touristhotspot',
            old_name='nome',
            new_name='name',
        ),
    ]
