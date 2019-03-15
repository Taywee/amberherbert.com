from wagtail.core import blocks

class Question(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.CharBlock(required=True)

    class Meta:
        template='faq/blocks/question.html'

class Category(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    questions = blocks.ListBlock(Question())

    class Meta:
        template='faq/blocks/category.html'
