# Generated by Django 4.2 on 2025-02-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnect', '0003_alter_pass_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='password',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
