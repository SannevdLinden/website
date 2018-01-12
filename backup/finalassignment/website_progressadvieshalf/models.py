from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers #for api
from pygments.styles import get_all_styles #for api
from pygments.lexers import get_lexer_by_name #for api
from pygments.formatters.html import HtmlFormatter #for api
from pygments import highlight #for api

LEXERS = [item for item in get_all_lexers() if item[1]] #indentify options for certain columns in Post
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Post(models.Model): #Post model which stores all the data for the todo's
    author = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, default=False)
    title = models.CharField(default=" ", max_length=200)
    text = models.TextField(default=" ")
    #number = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        #Use the `pygments` library to create a highlighted HTML
        #representation of the code snippet.
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.text, lexer, formatter)
        super(Post, self).save(*args, **kwargs)


    class Meta:
        ordering = ('created_date',)


#newnew
class Depthdata(models.Model):
    author = models.ForeignKey('auth.User', default=False)
    title = models.CharField(default="data",max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Bpdata(models.Model):
    author = models.ForeignKey('auth.User', default=False)
    title = models.CharField(default="data",max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Frdata(models.Model):
    author = models.ForeignKey('auth.User', default=False)
    title = models.CharField(default="data",max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Speeddata(models.Model):
    author = models.ForeignKey('auth.User', default=False)
    title = models.CharField(default="data",max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
