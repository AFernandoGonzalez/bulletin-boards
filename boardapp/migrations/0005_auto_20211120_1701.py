# Generated by Django 3.2.9 on 2021-11-20 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0004_alter_flyer_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flyer',
            name='due_date',
        ),
        migrations.AlterField(
            model_name='flyer',
            name='updated_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]