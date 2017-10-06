from django import template
from wagtail.wagtailcore.models import Page

from amber.models import NavigationPage, Banner

register = template.Library()

@register.assignment_tag
def get_navigation_items():
    return Page.objects.all().live().type(NavigationPage)

@register.assignment_tag
def get_banner():
    return Banner.objects.all().live().first()
