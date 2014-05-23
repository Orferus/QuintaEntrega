from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^projects/', include('ProjectsApp.urls', namespace="ProjectsManagement")),
    url(r'^admin/', include(admin.site.urls)),
)
