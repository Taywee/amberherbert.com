from django import template
from wagtail.wagtailcore.models import Page

from amber.models import NavigationPage

register = template.Library()

@register.assignment_tag
def get_navigation_items():
    return Page.objects.all().live().type(NavigationPage)
