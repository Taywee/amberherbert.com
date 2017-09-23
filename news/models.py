from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtailnews.models import NewsIndexMixin, AbstractNewsItem, AbstractNewsItemRevision
from wagtailnews.decorators import newsindex

@newsindex
class NewsIndex(NewsIndexMixin, Page):
    # Add extra fields here, as in a normal Wagtail Page class, if required
    newsitem_model = 'NewsItem'


class NewsItem(AbstractNewsItem):
    title = models.CharField(max_length=255)
    body = RichTextField()

    panels = [
        FieldPanel('title', classname='full title'),
        FieldPanel('body', classname='full'),
    ] + AbstractNewsItem.panels

    def __str__(self):
        return self.title

class NewsItemRevision(AbstractNewsItemRevision):
    newsitem = models.ForeignKey(NewsItem, related_name='revisions')
