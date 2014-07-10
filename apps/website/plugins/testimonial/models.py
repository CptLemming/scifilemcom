from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_text_ckeditor.fields import HTMLField


class Testimonial(CMSPlugin):
    title = models.CharField(_('Title'), blank=True, max_length=128)
    copy = HTMLField(_('Copy'))
    cite = models.CharField(_('Cite'), max_length=128)

    def __unicode__(self):
        return self.title
