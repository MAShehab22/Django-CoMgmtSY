from django.urls import path, include
from . import views



urlpatterns = [
   
    path('', views.employee_list),
     path('<int:id>', views.employee_details),
]