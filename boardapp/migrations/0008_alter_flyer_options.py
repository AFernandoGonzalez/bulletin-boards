# Generated by Django 3.2.9 on 2021-11-21 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0007_flyer_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flyer',
            options={'ordering': ['-id']},
        ),
    ]