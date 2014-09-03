__author__ = 'Zhanxueyou'
from django import template
import datetime
register = template.Library()


@register.filter(name='cut')    # 注册自定义过滤器
def cut(value, arg):
    return value.replace(arg, '')

@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tage requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])


class CurrentTimeNode(template.Node):
    def __init__(self, formate_string):
        self.format_string = str(formate_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime()

