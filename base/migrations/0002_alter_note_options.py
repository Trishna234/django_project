# Generated by Django 5.0.6 on 2024-06-20 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-id']},
        ),
    ]