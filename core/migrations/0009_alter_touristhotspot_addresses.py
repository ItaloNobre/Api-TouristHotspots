# Generated by Django 4.1.4 on 2022-12-17 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('core', '0008_touristhotspot_addresses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristhotspot',
            name='Addresses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.address'),
        ),
    ]
