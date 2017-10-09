from django import template
from wagtail.wagtailcore.models import Page

from news.models import NewsIndex

register = template.Library()

@register.assignment_tag
def get_news_index():
    '''Gets the first active news index in the list.  There should only be
    one'''

    return NewsIndex.objects.all().live().first()
