from django.conf.urls import patterns, include, url
from django.views.generic import DetailView
from activities.models import Activity
from activities import views
from leaves import views as leaves_views
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),

    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),

    url(r'^logout/$', views.logout_view, name="logout"),

    url(r'^reports/$', views.reports, name="reports"),

    url(r'^myreports/$', views.my_reports, name="my_reports"),

    url(r'^activity/edit/(?P<pk>\d+)', login_required(views.ActivityUpdate.as_view()),
                                       name="activity_edit"),

    url(r'^activity/delete/(?P<pk>\d+)', login_required(views.ActivityDelete.as_view()),
                                         name="activity_delete"),

    url(r'^all/$', views.all_activities, name="all_activities"),

    url(r'^redmine/$', views.redmine, name="redmine"),

    url(r'^leaves/$', leaves_views.index, name="leaves_index"),

    url(r'^admin/', include(admin.site.urls))
)
