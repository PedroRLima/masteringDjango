from django.conf.urls import include, url
from django.contrib import admin
from .views import hello, time_now, hours_ahead
from books.views import search


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', time_now),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', search),
]
