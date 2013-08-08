from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from activities.models import Activity
from activities import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),

    url(r'^activity/$',
        ListView.as_view(
            queryset=Activity.objects.order_by("activity_date"),
            context_object_name="results",
            template_name="activities/list.html"),
        name="activity_listing"),

    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),

    url(r'^logout/$', views.logout_view, name="logout"),

    url(r'^admin/', include(admin.site.urls)),
)
