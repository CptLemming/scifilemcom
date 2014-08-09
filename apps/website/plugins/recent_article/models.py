from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField


class RecentArticle(CMSPlugin):
    title = models.CharField(_('Title'), max_length=128)
    items_per_column = models.PositiveIntegerField(_('Items per column'), default=5)

    def copy_relations(self, oldinstance):
        for item in oldinstance.items.all():
            item.pk = None
            item.plugin = self
            item.save()

    def __unicode__(self):
        return self.title


class Item(models.Model):
    plugin = models.ForeignKey(RecentArticle, related_name='items')
    link_page = PageField(verbose_name=_('page'), related_name='recent_article_link', null=True)
    link_text = models.CharField(_('Link Text'), max_length=255, blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('position',)

    def __unicode__(self):
        return self.link_text