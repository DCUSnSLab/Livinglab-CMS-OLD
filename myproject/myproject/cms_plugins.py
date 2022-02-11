from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import Poem

@plugin_pool.register_plugin
class PoetryPlugin(CMSPluginBase):
    # model = CMSPlugin
    model = Poem
    render_template = "mypoems.html"
    cache = False