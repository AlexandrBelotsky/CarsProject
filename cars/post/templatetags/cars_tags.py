from django import template
from post.models import *


register = template.Library()

@register.simple_tag()
def get_category():
    return Category.objects.all()


