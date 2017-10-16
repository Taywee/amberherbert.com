from wagtail.wagtailcore import blocks

class Chapter(blocks.StructBlock):
    title = blocks.CharBlock()
    questions = blocks.RichTextBlock(required=True)

    class Meta:
        template='publish/blocks/chapter.html'
