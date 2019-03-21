from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, StreamFieldPanel)
from wagtail.core.blocks import (
    CharBlock, ListBlock, StructBlock, PageChooserBlock)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image

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

    background_image = models.ForeignKey(
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
            ImageChooserPanel('background_image'),
        ], 'Banner'),
        StreamFieldPanel('navigation'),
        FieldPanel('body', classname="full"),
    ]
