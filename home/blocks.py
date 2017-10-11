from wagtail.wagtailcore import blocks

class NavigationItem(blocks.StructBlock):
    text = blocks.CharBlock(required=True, min_length=2, max_length=16)
    page = blocks.PageChooserBlock(required=True)

    class Meta:
        template='home/blocks/navigation_item.html'
