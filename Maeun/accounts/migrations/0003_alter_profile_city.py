# Generated by Django 5.0 on 2023-12-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('Riyadh', 'Riyadh'), ('Jeddah', 'Jeddah'), ('Damamm', 'Damamm')], default='Riyadh', max_length=64),
        ),
    ]
