__author__ = 'Administrator'

from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def welcome(request):
    # html = "<html><head><title>My first project!</title></head><body>欢迎我的的第一个项目!</body></html>"
    current_date = datetime.datetime.now()
    return render_to_response('welcome.html', locals())
