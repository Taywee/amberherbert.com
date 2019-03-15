from wagtail.core import blocks

class Chapter(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = blocks.RichTextBlock(required=True)

    class Meta:
        template='publish/blocks/chapter.html'
