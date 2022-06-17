from django_filters import FilterSet
from .models import Post, PostCategory, Author



class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'title':['icontains'],
                  'rating': ['gt']}