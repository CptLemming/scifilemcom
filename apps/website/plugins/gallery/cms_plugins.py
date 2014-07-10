from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import StackedInline

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Gallery, Item


class ItemInline(StackedInline):
    model = Item
    extra = 0
    raw_id_fields = ('image',)


class GalleryPlugin(CMSPluginBase):
    model = Gallery
    name = _('Gallery')
    render_template = 'website/plugins/gallery.html'
    inlines = (ItemInline,)

    def render(self, context, instance, placeholder):
        context.update({
            'items': instance.items.all(),
            'instance': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(GalleryPlugin)
