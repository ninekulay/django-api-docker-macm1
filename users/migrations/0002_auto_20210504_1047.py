# Generated by Django 3.0 on 2021-05-04 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='title',
            field=models.CharField(max_length=16),
        ),
    ]
