# Generated by Django 3.2.12 on 2022-10-01 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_team_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='empolyee',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.team'),
        ),
    ]
