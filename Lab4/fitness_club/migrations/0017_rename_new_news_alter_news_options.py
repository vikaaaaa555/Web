# Generated by Django 4.2.5 on 2023-09-15 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_club', '0016_new_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New',
            new_name='News',
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
