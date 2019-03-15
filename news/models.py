from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtailnews.models import NewsIndexMixin, AbstractNewsItem, AbstractNewsItemRevision
from wagtailnews.decorators import newsindex

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
    newsitem = models.ForeignKey(NewsItem, related_name='revisions', on_delete=models.CASCADE)

@newsindex
class NewsIndex(NewsIndexMixin, Page):
    newsitem_model = NewsItem
    subpage_types = []
