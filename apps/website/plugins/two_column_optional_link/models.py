from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PageField


class TwoColumnOptionalLink(CMSPlugin):
    title = models.CharField(_('Title'), help_text=_('For admin only'), max_length=128)
    left_col = HTMLField(_('Left column'))
    right_col = HTMLField(_('Right column'))
    link_page = PageField(verbose_name=_('page'), related_name='two_column_optional_link', null=True)
    link_text = models.CharField(_('Link Text'), max_length=255, blank=True)

    def __unicode__(self):
        return self.title
