from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TwoColumnOptionalLink


class TwoColumnOptionalLinkPlugin(CMSPluginBase):
    model = TwoColumnOptionalLink
    name = _('Two Column Optional Link')
    render_template = 'website/plugins/two_column_optional_link.html'


plugin_pool.register_plugin(TwoColumnOptionalLinkPlugin)
