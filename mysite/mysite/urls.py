from django.conf.urls import patterns, include, url
from django.conf.urls import *
from mysite.views import *
from mysite.books.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})$/', hours_ahead),

    url(r'^admin/', include(admin.site.urls)),    # 这个地方如果在匹配末尾家$就会报错 NoReverseMatch at /admin/
    (r'^cur_url/$', current_url_view),
    (r'^display_meta/$', display_meta),
    (r'^search/$', search),
    (r'^contact/$', contact)
)
