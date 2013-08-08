from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'timesheet.views.home', name='home'),
    # url(r'^timesheet/', include('timesheet.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
