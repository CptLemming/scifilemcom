from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import StackedInline

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import FullWidthImageSlider, Slide


class SlideInline(StackedInline):
    model = Slide
    extra = 0
    raw_id_fields = ('image',)


class FullWidthImageSliderPlugin(CMSPluginBase):
    model = FullWidthImageSlider
    name = _('Full Width Image Slider')
    render_template = 'website/plugins/full_width_image_slider.html'
    inlines = (SlideInline,)

    def render(self, context, instance, placeholder):
        context.update({
            'slides': instance.slides.all(),
            'instance': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FullWidthImageSliderPlugin)
