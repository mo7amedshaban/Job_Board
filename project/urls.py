# -------->project/url.py

from django.contrib import admin
from django.template.backends import django
from django.urls import include, path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [  # this arrange for overwrite
    path('accounts/', include('django.contrib.auth.urls')),  # for login register
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('admin/', admin.site.urls),
    path('jobs/', include('job.urls', namespace="jobs")),
    path('contact-us/', include('contact.urls', namespace="contact")),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
