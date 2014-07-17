# /usr/bin
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse
import datetime


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = Template("<html><body></body>It is now {{ current_date }}</html>")
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)

# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template('current_datetime.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)

# def current_datetime(request):
#     now = datetime.datetime.now()
#     return render_to_response('current_datetime.html', {'current_date': now})

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime.html', locals())


def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<head><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def current_url_view(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


def display_meta(request):
    values = sorted(request.META.items())
    # values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

# HttpRequest的两个属性，两个类字典对象，request.GET、request.POST，类字典对象拥有一些普通字典所没有的方法



