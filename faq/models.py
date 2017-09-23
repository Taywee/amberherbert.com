from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class FAQIndex(Page):
    subpage_types = ['faq.FAQCategory']

class FAQCategory(Page):
    parent_page_types = ['faq.FAQIndex']
    subpage_types = ['faq.FAQQuestion']

class FAQQuestion(Page):
    question = RichTextField(verbose_name='Question')
    answer = RichTextField(verbose_name='Answer')

    content_panels = Page.content_panels + [
        FieldPanel('question', classname="full"),
        FieldPanel('answer', classname="full"),
    ]

    parent_page_types = ['faq.FAQCategory']
