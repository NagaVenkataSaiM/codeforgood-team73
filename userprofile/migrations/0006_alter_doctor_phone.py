# Generated by Django 4.0.5 on 2022-06-25 13:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_alter_doctor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
