from django.utils.translation import ugettext_lazy as _
from django.db import models

from filer.fields.image import FilerFileField

from cms.models import CMSPlugin


class FullWidthImageSlider(CMSPlugin):
    title = models.CharField(_('Title'), help_text=_('Admin only'), max_length=255, blank=True)

    def copy_relations(self, oldinstance):
        for item in oldinstance.slides.all():
            item.pk = None
            item.plugin = self
            item.save()

    def __unicode__(self):
        return self.title


class Slide(models.Model):
    plugin = models.ForeignKey(FullWidthImageSlider, related_name='slides')
    image = FilerFileField(related_name='full_width_image_slider_image')
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('position',)

    def __unicode__(self):
        return self.image.original_filename
