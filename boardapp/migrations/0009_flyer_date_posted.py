# Generated by Django 3.2.9 on 2021-12-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0008_alter_flyer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyer',
            name='date_posted',
            field=models.DateField(null=True),
        ),
    ]