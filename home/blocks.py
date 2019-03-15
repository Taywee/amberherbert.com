from wagtail.core import blocks

class NavigationItem(blocks.StructBlock):
    text = blocks.CharBlock(
        required=False,
        max_length=16,
        help_text=(
            "If this is left blank, the title of the linked page will be used "
            "instead")
    )
    page = blocks.PageChooserBlock(required=True)

    class Meta:
        template='home/blocks/navigation_item.html'
