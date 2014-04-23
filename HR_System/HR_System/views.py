__author__ = 'Administrator'

from django.http import HttpResponse


def welcome(request):
    html = "<html><head><title>My first project!</title></head><body>欢迎我的的第一个项目!</body></html>"
    return HttpResponse(html)