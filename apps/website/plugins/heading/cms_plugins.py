from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Heading


class HeadingPlugin(CMSPluginBase):
    model = Heading
    name = _('Heading')
    render_template = 'website/plugins/heading.html'


plugin_pool.register_plugin(HeadingPlugin)
