from django.conf.urls.defaults import *

urlpatterns = patterns('autocomplete.views',
    url(r'^tags/$', 'autocomplete_tags', name='autocomplete-tags'),
    url(r'^m2m/$', 'autocomplete_m2m', name='autocomplete-m2m'),
)
