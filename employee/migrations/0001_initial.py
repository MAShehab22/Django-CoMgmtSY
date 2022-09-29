# Generated by Django 4.1.1 on 2022-09-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empolyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employee_id', models.IntegerField()),
                ('team_part', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3')], max_length=100)),
                ('hourly_rate', models.IntegerField(choices=[(15, '15'), (20, '20'), (30, '30')])),
            ],
        ),
    ]
