from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers #voor api
from pygments.styles import get_all_styles #voor api
from pygments.lexers import get_lexer_by_name #step 4
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]] #vanaf hier tot einde voor API
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Post(models.Model): #name is Post and can be changed
    author = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, default=False)
    title = models.CharField(max_length=200)
    text = models.TextField()
    #number = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField(default=False)#step4

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): #step4
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
        #ordering = ('created',)






"""

class Post(models.Model): #name is Post and can be changed
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    #number = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, default=False) #step4
    highlighted = models.TextField(default=False)#step4

    def save(self, *args, **kwargs): #step4
        #Use the `pygments` library to create a highlighted HTML
        #representation of the code snippet.
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


    class Meta:
        ordering = ('created',)
"""
