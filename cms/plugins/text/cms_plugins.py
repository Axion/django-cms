
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from models import Text
from cms.plugins.text.forms import TextForm
from cms.plugins.text.utils import plugin_tags_to_user_html


class TextPlugin(CMSPluginBase):
    model = Text
    name = _("Text")
    form = TextForm
    render_template = "cms/plugins/text.html"
    change_form_template = "cms/plugins/text_plugin_change_form.html"

    def render(self, context, instance, placeholder):
        if settings.CMS_DBGETTEXT:
            from dbgettext.parser import parsed_gettext
            instance.body = parsed_gettext(instance, 'body')
        context.update({
            'body': plugin_tags_to_user_html(instance.body, context, placeholder),
            'placeholder': placeholder,
            'object': instance
        })
        return context

plugin_pool.register_plugin(TextPlugin)
