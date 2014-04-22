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
    (r'^time/plus/(\d+)/$', hours_ahead),   # 这里需要注意，调用哪个参数的位置的模式匹配必须有括号
    #(r'^time/plus/\d+/$', hours_ahead),    # 这样写是不对的，会有错误产生
    #url(r'^admin/', include(admin.site.urls)),
)
