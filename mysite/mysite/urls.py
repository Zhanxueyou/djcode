from django.conf.urls import patterns, include, url
from django.conf.urls import *
from mysite.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})$/', hours_ahead),

    url(r'^admin/', include(admin.site.urls)),
)
