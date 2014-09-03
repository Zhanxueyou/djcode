from django.db import models


class BookManager(models.Manager):      # 自定义manager方法
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')   # 在管理工具中可以不填，同时在数据库中也展现了字段的属性
    # email = models.EmailField('e-mail', blank=True)   该句与上句等价，但是并不适用于ManyToManyField和ForeignKey字段

    # def __unicode__(self):
    #     return '%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    num_page = models.IntegerField(blank=True, null=True)
    num_page_test = models.IntegerField(null=True)
    objects = BookManager()

    # def __unicode__(self):
    #     return self.title
