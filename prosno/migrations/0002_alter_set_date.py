# Generated by Django 4.1.2 on 2022-10-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prosno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='date',
            field=models.DateField(),
        ),
    ]
