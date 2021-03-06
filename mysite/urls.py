from django.conf.urls import include, url
from django.contrib import admin
from .views import time_now, hours_ahead, contact
from books.views import search


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', time_now),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
]
