from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class NavigationPage(Page):
    '''A page that is put into the navigation menu'''
    nav_text = models.TextField(
        verbose_name='Navigation Text',
        help_text='The text that appears in the navigation element')

    content_panels = Page.content_panels + [
        FieldPanel('nav_text', classname="full"),
    ]

    class Meta:
        abstract = True
        
class SimplePage(NavigationPage):
    '''A navigatable page with a simple RichTextField body'''
    body = RichTextField(blank=True)

    content_panels = NavigationPage.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class Banner(Page):
    '''A banner type, defining the banner of the site.'''

    image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+')

    content_panels = Page.content_panels + [
        ImageChooserPanel('image')
        ]
