from django.conf.urls.defaults import *

urlpatterns = patterns('textext.views',
    url(r'^search/$', 'search_tags', name='textext-search'),
)
