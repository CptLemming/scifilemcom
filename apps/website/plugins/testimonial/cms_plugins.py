from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Testimonial


class TestimonialPlugin(CMSPluginBase):
    model = Testimonial
    name = _('Testimonial')
    render_template = 'website/plugins/testimonial.html'


plugin_pool.register_plugin(TestimonialPlugin)