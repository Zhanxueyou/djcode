from django.contrib import admin
from mysite.books.models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')     # 管理界面显示列表
    search_fields = ('first_name', 'last_name')             # 管理界面的搜索框
    fields = ('first_name', 'last_name', 'email',)          # 编辑表单时需要显示的项


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)                     # 创建了一个过滤器，位于列表页面的右边
    date_hierarchy = 'publication_date'                     # 在页面顶端装一个逐层深入的分级导航条
    ordering = ('-publication_date',)                       # 添加一个默认排序
    # fields = ('title', 'authors', 'publisher',)  # 在编辑表单时需要显示的项和顺序，这样就可以排除一些不想让别人编辑的表单选项
    filter_horizontal = ('authors',)                        # 编辑表单时的水平过滤器，只能用在多对多字段上
    raw_id_fields = ('publisher',)                          # 把外键装载到一个文本框中，而不是下拉框中，如果数据太多，下拉框会导致加载页面时间过长


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'country', 'website')    # 显示列表

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)    # 用AuthorAdmin注册Author模块
admin.site.register(Book, BookAdmin)

