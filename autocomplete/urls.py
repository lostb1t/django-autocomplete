from django.conf.urls.defaults import *

urlpatterns = patterns('autocomplete.views',
    url(r'^search/$', 'search_tags', name='autocomplete-search'),
)
