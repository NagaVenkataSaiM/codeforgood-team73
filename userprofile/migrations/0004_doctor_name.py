# Generated by Django 4.0.5 on 2022-06-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_remove_doctor_name_doctor_city_doctor_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
