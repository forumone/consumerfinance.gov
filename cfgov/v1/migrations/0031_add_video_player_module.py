# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import v1.atomic_elements.organisms


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0030_adjust_feedback_default_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'image_text_25_75_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])))])), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'}))])), (b'expandable', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])), (b'expandable_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_accordion', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'expandables', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'call_to_action', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use this field only for feedback forms that use "Was this helpful?" radio buttons.', default=b'Was this page helpful to you?', required=False)), (b'intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional feedback intro', required=False)), (b'question_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional expansion on intro', required=False)), (b'radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), (b'radio_text', wagtail.wagtailcore.blocks.CharBlock(default=b'This information helps us understand your question better.', required=False)), (b'radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default=b'How soon do you expect to buy a home?', required=False)), (b'radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default=b'Do you currently own a home?', required=False)), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit')), (b'contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Use only for feedback forms that ask for a contact email', required=False))])), (b'video_player', wagtail.wagtailcore.blocks.StructBlock([(b'video_url', wagtail.wagtailcore.blocks.RegexBlock(regex=b'^https:\\/\\/www\\.youtube\\.com\\/embed\\/[a-zA-Z0-9]+([/]?)$', default=b'https://www.youtube.com/embed/', required=True, error_messages={b'required': b'The YouTube URL field is required for video players.', b'invalid': b'The YouTube URL is in the wrong format. You must use the embed URL (https://www.youtube.com/embed/video_id), which can be obtained by clicking Share > Embed on the YouTube video page.'}, label=b'YouTube Embed URL'))]))], blank=True),
        ),
    ]
