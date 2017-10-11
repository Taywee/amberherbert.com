from django import template
from wagtail.wagtailcore.models import Page

from home.models import HomePage

register = template.Library()

@register.assignment_tag
def get_home_page():
    '''Gets the first active home page in the list.  There should only be
    one'''

    return HomePage.objects.all().live().first()
