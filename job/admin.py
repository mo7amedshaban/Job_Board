from django.contrib import admin

# Register your models here.

from .models import Job, Categories, Apply

admin.site.register(Job)
admin.site.register(Categories)
admin.site.register(Apply)
