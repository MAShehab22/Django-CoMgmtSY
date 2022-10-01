from django.contrib import admin

# Register your models here.
from .models import empolyee, Work_arrangement, Team, Team_leader, Team_employee
admin.site.register(empolyee)
admin.site.register(Work_arrangement)
admin.site.register(Team)
admin.site.register(Team_leader)
admin.site.register(Team_employee)
