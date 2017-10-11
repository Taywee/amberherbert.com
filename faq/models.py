from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import CharBlock, ListBlock, StructBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

class FAQIndex(Page):
    body = StreamField([
        ('category', StructBlock([
            ('name', CharBlock(required=True)),
            ('questions', ListBlock(StructBlock([
                ('question', CharBlock(required=True)),
                ('answer', CharBlock(required=True)),
            ],
            template='faq/blocks/question.html'
            ))),
        ],
        template='faq/blocks/category.html'
        ))],
        blank=True,
        null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
