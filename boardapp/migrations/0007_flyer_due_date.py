# Generated by Django 3.2.9 on 2021-11-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0006_flyer_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyer',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
