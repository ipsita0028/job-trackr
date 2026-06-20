from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_list),          #GET all jobs, POST new job
    path('jobs/<int:pk>/', views.job_detail),  #GET, PUT, DELETE one job by ID
]