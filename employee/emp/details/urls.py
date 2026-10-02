from django.urls import path
from . import views

urlpatterns = [
    path('emp_details/', views.emp_details, name='emp_details')
]
