from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField

from cms.models import CMSPlugin
from cms.models.fields import PageField

from djangocms_text_ckeditor.fields import HTMLField


class ReadMoreGrid(CMSPlugin):
    TOP_GRID = 'top-grid'
    MID_GRID = 'mid-grid'

    CHOICES = (
        (TOP_GRID, _('Top Grid')),
        (MID_GRID, _('Mid Grid')),
    )

    title = models.CharField(_('Title'), help_text=_('Admin Only'), max_length=128)
    type = models.CharField(_('Type'), choices=CHOICES, default=TOP_GRID, max_length=128)

    def copy_relations(self, oldinstance):
        for item in oldinstance.items.all():
            item.pk = None
            item.plugin = self
            item.save()

    def get_type(self):
        return self.type

    def get_type_plural(self):
        return self.type + 's'

    def __unicode__(self):
        return self.title


class Item(models.Model):
    plugin = models.ForeignKey(ReadMoreGrid, related_name='items')
    title = models.CharField(_('Title'), max_length=128)

    icon = FilerImageField(related_name='read_more_icon')
    copy = HTMLField(_('Copy'))
    link_page = PageField(verbose_name=_('page'), related_name='read_more_link', null=True)
    link_text = models.CharField(_('Link Text'), max_length=255, blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('position',)

    def __unicode__(self):
        return self.title
