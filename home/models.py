from django.db import models

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, StreamFieldPanel)
from wagtail.wagtailcore.blocks import (
    CharBlock, ListBlock, StructBlock, PageChooserBlock)
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image

from .blocks import NavigationItem

class HomePage(Page):
    body = RichTextField(blank=True)

    banner_text = models.CharField(
        blank=True,
        null=True,
        max_length=64,
        help_text='This is the text that is displayed with the banner image',
        default='Amber Herbert')

    banner_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+')

    navigation = StreamField(
        [('item', NavigationItem())],
        blank=True,
        null=True,
        help_text="The list of navigation items")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('banner_text'),
            ImageChooserPanel('banner_image'),
        ], 'Banner'),
        StreamFieldPanel('navigation'),
        FieldPanel('body', classname="full"),
    ]
