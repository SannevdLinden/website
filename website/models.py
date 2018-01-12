# From here added by Lars----------------------------------------------------------------
from __future__ import unicode_literals
# Till here added by Lars----------------------------------------------------------------
from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers #for api
from pygments.styles import get_all_styles #for api
from pygments.lexers import get_lexer_by_name #for api
from pygments.formatters.html import HtmlFormatter #for api
from pygments import highlight #for api
import datetime #ADDED!!
from django.core.exceptions import ValidationError #ADDED
from django.urls import reverse #ADDED

# From here added by Lars----------------------------------------------------------------
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Till here added by Lars----------------------------------------------------------------


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


# THIS HAS BEEN ADDED!
class Event(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=False)
    number = models.CharField(u'Session ID', help_text=u'Session ID', max_length=5, null=True)
    day = models.DateField(u'Day of the event (JJJJ-MM-DD)', help_text=u'Day of the event in JJJJ-MM-DD')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    place = models.CharField(u'Location', help_text=u'Location', max_length=25, null=True)
    instructor = models.CharField(u'Instructor(s)', help_text=u'Instructor(s)', max_length=50, null=True)
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

#def get_absolute_url(self):
#	return "/admin/events"

class Meta:
	ordering = ["-day"]
verbose_name = "event"
verbose_name_plural = "events"

class Blog(models.Model): #Sebastiaan
    author = models.ForeignKey('auth.User')
    Title = models.CharField(max_length=200)
    Text =  models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(
            default=timezone.now)
    flags = models.IntegerField(default=0,
            blank=True, null=True)



    def publish(self): #Sebastiaan
        self.published_date = timezone.now()
        self.save()

class Comment(models.Model): #Sebastiaan
    blog = models.ForeignKey('website.Blog', related_name='comments')
    author = models.ForeignKey('auth.User')
    target = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def publish(self): #Sebastiaan
        self.save()

    def __str__(self):
        return self.text

class Flagged(models.Model): #SebastiaanNEW
    blog = models.ForeignKey('website.Blog', related_name='flagged')
    username = models.ForeignKey('auth.User')
    flagdate = models.DateTimeField(default=timezone.now)


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

class Colorsetting(models.Model):
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

# From here added by Lars----------------------------------------------------------------

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

# Till here added by Lars----------------------------------------------------------------
