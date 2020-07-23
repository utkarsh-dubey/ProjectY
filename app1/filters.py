import django_filters
from django_filters import CharFilter

from .models import *

class PostFilter(django_filters.FilterSet):

    title = CharFilter(field_name='title', lookup_expr = 'icontains')
    user = CharFilter(field_name='user', lookup_expr = 'icontains')


    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['content', 'url']
