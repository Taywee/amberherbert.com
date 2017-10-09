from django.db import models

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from amber.models import NavigationPage

class HomePage(NavigationPage):
    body = RichTextField(blank=True)

    content_panels = NavigationPage.content_panels + [
        FieldPanel('body', classname="full"),
    ]
