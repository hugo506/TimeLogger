from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from activities.models import Activity
from activities import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),

    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),

    url(r'^logout/$', views.logout_view, name="logout"),

    url(r'^reports/$', views.reports, name="reports"),

    url(r'^all/$', views.all_activities, name="all_activities"),

    url(r'^admin/', include(admin.site.urls)))
