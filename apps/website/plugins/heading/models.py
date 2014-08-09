from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class Heading(CMSPlugin):
    title = models.CharField(_('Title'), max_length=256)

    def __unicode__(self):
        return self.title
