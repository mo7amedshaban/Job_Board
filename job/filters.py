import django_filters  # don't worry about this
from .models import Job


class JobFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(
        lookup_expr='icontains')  # this for search exist if one word in description statement
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner', 'slug', 'published_at', 'image', 'salary', 'vacancy']  # not apear in form
