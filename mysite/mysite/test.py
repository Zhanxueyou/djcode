__author__ = 'Zhanxueyou'
def application(env, start_response):
    start_response('200 OK!',[('Content_Type','text/html')])
    return "uWSGI Testing OK!!!"