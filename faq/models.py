from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import CharBlock, ListBlock, StructBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

from .blocks import Category

class FAQIndex(Page):
    body = StreamField(
        [('category', Category())],
        blank=True,
        null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
