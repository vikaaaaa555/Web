# Generated by Django 4.2.1 on 2023-06-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_club', '0002_client_age_client_email_client_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='client_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
