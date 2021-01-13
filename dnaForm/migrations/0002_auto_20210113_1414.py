# Generated by Django 3.1.2 on 2021-01-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnaForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequencesearch',
            name='protein_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sequencesearch',
            name='protein_sequence',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
