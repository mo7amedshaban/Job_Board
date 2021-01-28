from django import forms
from .models import Apply, Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']  # here i not use job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'  # use all fields
        exclude = ('owner', 'slug',)  # not use field slug
