from django import forms

from .models import Post, Event, Blog, Comment #ADDED

# From here added by Lars----------------------------------------------------------------

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Profile

# Till here added by Lars----------------------------------------------------------------


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text',)

#ADDED
class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('number', 'day', 'start_time', 'end_time', 'place', 'instructor', 'notes',)

class BlogForm(forms.ModelForm):#Sebastiaan
    class Meta:#Sebastiaan
        model = Blog#Sebastiaan
        fields = ('Title','Text',)
        #docfile = forms.FileField(label='Select a file',)
class CommentForm(forms.ModelForm): #Sebastiaan

    class Meta:
        model = Comment
        fields = ('text',)

# From here added by Lars----------------------------------------------------------------

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        #fields = ('username', 'birth_date', 'password1', 'password2', )
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )

#class UserForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('first_name', 'last_name', 'email')

#class ProfileForm(forms.ModelForm):
#    class Meta:
#        model = Profile
#        fields = ('url', 'location', 'company')

# Till here added by Lars----------------------------------------------------------------
