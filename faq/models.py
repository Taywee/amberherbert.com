from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import CharBlock, ListBlock, StructBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import Category

class FAQIndex(Page):
    body = StreamField(
        [('category', Category())],
        blank=True,
        null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    subpage_types = []
