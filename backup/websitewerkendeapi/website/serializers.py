from rest_framework import serializers
#from website.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from website.models import Post, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User #step4


class SnippetSerializer(serializers.HyperlinkedModelSerializer): #step5
    #owner = serializers.ReadOnlyField(source='owner.username')
    author = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    highlight = serializers.HyperlinkedIdentityField(view_name='post-highlight', format='html')

    class Meta:
        model=Post
        #model = Snippet
        #fields = ('url', 'id', 'highlight', 'owner',
        #          'title', 'code', 'linenos', 'language', 'style')

        fields = ('url', 'id', 'highlight', 'author',
                  'title', 'text', 'linenos', 'language', 'style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
