# Generated by Django 5.0.8 on 2024-08-20 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudante',
            old_name='data_nasscimento',
            new_name='data_nascimento',
        ),
    ]