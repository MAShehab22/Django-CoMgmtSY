# Generated by Django 4.1.1 on 2022-09-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_team_team_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_one', models.CharField(max_length=30)),
                ('Team_two', models.CharField(max_length=30)),
                ('Team_three', models.CharField(max_length=30)),
            ],
        ),
    ]