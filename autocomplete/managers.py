from django.utils.translation import ugettext_lazy as _
from django.utils.simplejson import loads

from taggit.forms import TagField
from taggit.managers import TaggableManager as BaseTaggableManager

from widgets import AutocompleteTags

class AutocompleteTagField(TagField):
    widget = AutocompleteTags

    def clean(self, value):
        words = loads(value)
        words.sort()
        return words

class TaggableManager(BaseTaggableManager):
    def formfield(self, form_class=AutocompleteTagField, **kwargs):
        defaults = {
            "label": _("Tags"),
            "help_text": "",
        }
        defaults.update(kwargs)
        kwargs['widget'] = AutocompleteTags
        return form_class(**kwargs)

from south.modelsinspector import add_ignored_fields
add_ignored_fields(["^autocomplete\.managers"])