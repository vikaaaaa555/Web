# Generated by Django 4.2.5 on 2023-09-14 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_club', '0014_coupon_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'News',
            },
        ),
    ]
