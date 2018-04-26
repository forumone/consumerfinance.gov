# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('regulations3k', '0003_alter_regulationpage_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulationpage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField([('text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'eyebrow', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', required=False, label=b'Pre-heading')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False)), (b'aria_label', wagtail.wagtailcore.blocks.CharBlock(help_text=b'If the main link text is not descriptive enough for a screen reader user, use this field to have a screen reader read something else in place of the link text.', required=False, label=b'ARIA label'))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to bottom of text introduction.', required=False, label=b'Has bottom rule'))]))], blank=True),
        ),
    ]
