from django.conf.urls import patterns, include, url
from HR_System.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HR_System.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^welcome/$', welcome)
    #url(r'^admin/', include(admin.site.urls)),
)
