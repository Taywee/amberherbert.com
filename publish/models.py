from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from .blocks import Chapter

class PublishedWorkTag(TaggedItemBase):
    content_object = ParentalKey('publish.PublishedWork', related_name='tagged_items')

class PublishedWork(Page):
    '''A type for online-published works.  This type should be properly
    indexed, searchable, taggable, and should provide some sort of built-in
    mechanism to split an individual published work into chapters with anchors
    (probably done via "chapter" blocks on a StreamField).  Chapters will
    probably be a simple string title + RichTextField body pair, with an
    optional empty title, as a single-chapter work wouldn't need a named title,
    and named titles shouldn't be mandatory, but even without named titles, we
    want to be able to link to the chapter.'''

    is_creatable = False

    summary = models.TextField(
        blank=True,
        null=True,
        help_text=(
            "This is shown at the top of the published work's own page and in "
            "search results.")
    )

    tags = ClusterTaggableManager(through=PublishedWorkTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        FieldPanel('tags'),
    ]

    parent_page_types = ['publish.PublishedWorkIndex']


class Poem(PublishedWork):
    '''A poetry-specific published work.'''

    body = RichTextField()

    content_panels = PublishedWork.content_panels + [
        FieldPanel('body'),
    ]

class ShortStory(PublishedWork):
    '''A short story published work.'''

    body = RichTextField()

    content_panels = PublishedWork.content_panels + [
        FieldPanel('body'),
    ]

class LongStory(PublishedWork):
    '''A long story (chapter-broken) published work.'''

    body = StreamField([('chapter', Chapter())])

    generate_navigation = models.BooleanField(
        verbose_name="Generate a navigation menu",
        default=True,
        help_text=(
            "This determines whether a navigation menu for chapters will be "
            "generated for this page")
    )

    content_panels = PublishedWork.content_panels + [
        StreamFieldPanel('body'),
        FieldPanel('generate_navigation'),
    ]

class PublishedWorkIndex(Page):
    '''An index page for published works.  Has a small body, but mostly acts as
    a cataloguing platform, allowing searching for works underneath it.'''

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    subpage_types = [
        Poem,
        ShortStory,
        LongStory,
    ]

    def get_context(self, request):
        tags = request.GET.get('tags')
        # Can not use get_children, as they need to be filterable by tag
        pages = PublishedWork.objects.child_of(self)
        if tags:
            tags = frozenset(tags.split(','))
            # Iteratively filter for all tags
            for tag in tags:
                pages = pages.filter(tags__name=tag)
        else:
            tags = frozenset()

        alltags = frozenset(
            tag.tag.name for tag in PublishedWorkTag.objects.filter(
                content_object__in=PublishedWork.objects.child_of(self)))

        context = super().get_context(request)
        context['pages'] = pages
        context['alltags'] = alltags
        context['selectedtags'] = tags
        context['unselectedtags'] = alltags - tags
        return context

