from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField

from cms.models import CMSPlugin

from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PageField


class WelcomeHero(CMSPlugin):
    title = models.CharField(_('Title'), max_length=128)
    copy = HTMLField(_('Copy'))
    image = FilerImageField(related_name='welcome_hero_image')
    link_page = PageField(verbose_name=_('page'), related_name='welcome_hero_link')
    link_text = models.CharField(_('Link Text'), max_length=255, blank=True)

    def __unicode__(self):
        return self.title
