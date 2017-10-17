from copy import copy
from django import template
from wagtail.wagtailcore.models import Page

from home.models import HomePage

register = template.Library()

@register.simple_tag
def tag_list(tags, add=None, remove=None):
    '''Takes a tag set and an optional added tag or removed tag, and returns
    the comma-separated tag value'''

    tags = copy(tags)

    if add is not None:
        tags = tags | {add}
    if remove is not None:
        tags = tags - {remove}

    return ','.join(tags)
