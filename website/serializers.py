from rest_framework import serializers
from website.models import Post, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User #step4
from .models import Event


class SnippetSerializer(serializers.HyperlinkedModelSerializer): #for the API to identify which information of the model Post is used
    author = serializers.ReadOnlyField(source='owner.username')
    highlighted = serializers.HyperlinkedIdentityField(view_name='post-highlighted', format='html')

    class Meta:
        model=Post
        fields = ('url', 'id', 'highlighted', 'author',
                  'title', 'text', 'linenos', 'language', 'style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')

#ADDED
class SessionSerializer(serializers.HyperlinkedModelSerializer): #for the API to identify which information of the model Post is used
    author = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model= Event
        fields = '__all__'
