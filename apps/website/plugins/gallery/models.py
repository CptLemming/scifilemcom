from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField

from cms.models import CMSPlugin


class Gallery(CMSPlugin):
    title = models.CharField(_('Title'), max_length=128)

    def copy_relations(self, oldinstance):
        for item in oldinstance.items.all():
            item.pk = None
            item.plugin = self
            item.save()

    def __unicode__(self):
        return self.title


class Item(models.Model):
    plugin = models.ForeignKey(Gallery, related_name='items')
    image = FilerImageField(related_name='gallery_image')
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('position',)

    def __unicode__(self):
        return self.image.original_filename
