from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'app.views.home'),
)

urlpatterns += staticfiles_urlpatterns()
