# Generated by Django 4.1.1 on 2022-09-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_remove_empolyee_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_arrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_time', models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time')], max_length=100)),
            ],
        ),
    ]
