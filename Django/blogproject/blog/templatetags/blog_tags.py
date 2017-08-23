from ..models import Post,Category
from django import template
register=template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('create_time','month',order='DESC')

@register.simple_tag
def get_category():
    return Category.objects.all()
