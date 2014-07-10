from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import WelcomeHero


class WelcomeHeroPlugin(CMSPluginBase):
    model = WelcomeHero
    name = _('Welcome Hero')
    render_template = 'website/plugins/welcome_hero.html'


plugin_pool.register_plugin(WelcomeHeroPlugin)
