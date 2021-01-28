from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from .form import ApplyForm, JobForm
from .models import Job
from .filters import JobFilter


def job_list(request):
    All_job_list = Job.objects.all()
    myfilter = JobFilter(request.GET, queryset=All_job_list)
    All_job_list = myfilter.qs

    p = Paginator(All_job_list, 4)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'jobs': page_obj, 'myfilter': myfilter}
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    All_job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)  # not make save
            myform.job = All_job_detail
            myform.save()
    else:  # if request.method=="GET" || any thing
        form = ApplyForm()  # empty form

    context = {'job': All_job_detail, 'form': form}
    return render(request, 'job/job_detail.html', context)


@login_required  # this is decorators   == middelware in laravel    --> decorator for add_job
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            # here not make for slug because slug in model save function use it
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    return render(request, 'job/add_job.html', {'form': form})
