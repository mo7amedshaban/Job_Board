# ------> job/urls.py
from django.urls import path
from . import api
from . import views

app_name = 'job'
urlpatterns = (
    path('', views.job_list, name='job_list'),
    path('add_job', views.add_job, name="add_job"),
    path('<str:slug>', views.job_detail, name="job_detail"),  # use slug last statement for run path

    path('api/job', api.joblistapi, name="joblistapi"),
)
