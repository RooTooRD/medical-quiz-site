# Generated by Django 5.0.7 on 2024-07-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
