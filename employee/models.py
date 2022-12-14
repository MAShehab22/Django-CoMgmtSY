from email.policy import default
from email.utils import parsedate_to_datetime
from mimetypes import read_mime_types
from random import choices
from re import A
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

hourly_rate_choices= [
        (15, '15'),
        (20, '20'),
        (30, '30'),
]   

ONE="One"
TWO="Two"
THREE="Three"



teams_choices= [
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
]


RAMY='Ramy'
HUSSAM='Hussam'
BAHAA='Bahaa'

team_leader_choices= [
        (RAMY, 'Ramy'),
        (HUSSAM, 'Hussam'),
        (BAHAA, 'Bahaa'),
]

""" team_employee_one_choices=['Ramy', 'Ezzat', 'Gamal' ]
team_employee_two_choices=['Hussam', 'Saleh', 'Sayed' ]
team_employee_three_choices=['Bahaa', 'Fady', 'Esraa' ] """




""" class Team(models.Model):
    Team_name = models.CharField(max_length=30, choices= teams_choices)
    
    def __str__(self):
        return (self.Team_name) """

class empolyee(models.Model):
    name = models.CharField(max_length=100)
    team_part = models.CharField(max_length=100, choices = teams_choices)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)
    work_arrangement = models.ForeignKey('Work_arrangement', on_delete=models.CASCADE, null=True)
    team_leader = models.ForeignKey('Team_leader', on_delete=models.CASCADE, null=True)
    hourly_rate = models.IntegerField(choices=hourly_rate_choices)
    team_employee = models.ManyToManyField('Team_employee', null=True)
    def __str__(self):
        return self.name


class Team(models.Model):
    Team_name = models.CharField(max_length=30, choices= teams_choices)
    
    def __str__(self):
        return (self.Team_name)

class Team_leader(models.Model):
    Team_leader_name = models.CharField(max_length=30, choices= team_leader_choices)
    
    def __str__(self):
        return (self.Team_leader_name)


class Team_employee(models.Model):
    """ Team_one = models.CharField(max_length=30)
    Team_two = models.CharField(max_length=30)
    Team_three = models.CharField(max_length=30) """

    Team_employee_CHOICES = [
    ('Team_one_employee', (
            ('ramy', 'Ramy'),
            ('ezzat', 'Ezzat'),
            ('gamal', 'Gamal'),
        )
    ),
    ('Team_two_employee', (
            ('hussam', 'Hussam'),
            ('saleh', 'Saleh'),
            ('sayed', 'Sayed'),
        )
    ),
        ('Team_three_employee', (
            ('bahaa', 'Bahaa'),
            ('fady', 'Fady'),
            ('esraa', 'Esraa'),
        )
    ),
    #('unknown', 'Unknown'),
]
    
    Team_employee_category = models.CharField(max_length=30, choices=Team_employee_CHOICES)
    def __str__(self):
        return (self.Team_employee_category)

class Work_arrangement(models.Model):
    fulltime = 'Full time'
    parttime = 'Part time'
    work_time_choices = [
        (fulltime, 'Full time'),
        (parttime, 'Part time'),
    ]
    work_time = models.CharField(max_length=100, choices = work_time_choices)
    
    def __str__(self):
        return (self.work_time)




        
