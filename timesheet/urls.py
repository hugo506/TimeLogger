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

    url(r'^add/$', views.add_activity, name="add_activity"),

    url(r'^admin/', include(admin.site.urls)),
)
