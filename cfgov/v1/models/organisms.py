from wagtail.wagtailcore import blocks


class Well(blocks.StructBlock):
    template_path = blocks.CharBlock(required=True)

    class Meta:
        icon = 'link'
        template = 'v1/demo/organisms/well.html'
