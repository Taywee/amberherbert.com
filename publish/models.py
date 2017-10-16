from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from .blocks import Chapter

class PublishedWorkIndex(Page):
    '''An index page for published works.  Has a small body, but mostly acts as
    a cataloguing platform, allowing searching for works underneath it.'''

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    subpage_types = ['publish.PublishedWork']

class PublishedWork(Page):
    '''A type for online-published works.  This type should be properly
    indexed, searchable, taggable, and should provide some sort of built-in
    mechanism to split an individual published work into chapters with anchors
    (probably done via "chapter" blocks on a StreamField).  Chapters will
    probably be a simple string title + RichTextField body pair, with an
    optional empty title, as a single-chapter work wouldn't need a named title,
    and named titles shouldn't be mandatory, but even without named titles, we
    want to be able to link to the chapter.'''

    summary = RichTextField(blank=True)

    body = StreamField([('chapter', Chapter())])

    content_panels = Page.content_panels + [
        FieldPanel('summary', classname="full"),
    ]

    parent_page_types = ['publish.PublishedWorkIndex']
