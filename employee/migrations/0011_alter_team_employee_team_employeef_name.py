# Generated by Django 3.2.12 on 2022-10-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20221001_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_employee',
            name='Team_employeef_name',
            field=models.CharField(choices=[('Team_one_employee', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Team_two_employee', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('Team_two_employee', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], max_length=30),
        ),
    ]
