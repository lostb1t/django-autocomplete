from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.simplejson import dumps
from taggit.models import Tag
from django.utils.translation import ugettext as _

RESULTS = getattr(settings, 'AUTOCOMPLETE_RESULTS_LIMIT', 20)

# TODO: Cache the results
def autocomplete_tags(request):
  try:
    query = request.GET['q']
    tags = Tag.objects.filter(name__icontains=query).values_list('name', flat=True)[:RESULTS]
    response = sorted(tags, key=lambda t: len(t))
    return HttpResponse(dumps(response), mimetype='application/json')
  except KeyError:
    return HttpResponseBadRequest()

def autocomplete_m2m(request):
  '''
  Ajax autocomplete for m2m fields
  '''
  data = []
  if request.method == 'GET':
    if request.GET.has_key('q') and request.GET.has_key('content_type_id'):
      q = request.GET.get("q")
      content_type_id = request.GET.get("content_type_id")
      ctype = ContentType.objects.get_for_id(int(content_type_id))
      searchable_models = [ctype.model_class(),] # Models to search
      objects = []
      for bit in q.split():
        for model in searchable_models:
          search = [models.Q(**{smart_str(item):smart_str(bit)}) for item in model.autocomplete_search_fields()]
          search_qs = QuerySet(model)
          search_qs = search_qs.filter(reduce(operator.or_, search))
          objects = objects + list(search_qs[:10])
          
      data = [{"value":u'%s' % get_value(f),"label":u'%s' % get_label(f)} for f in objects[:10]]
      label = ungettext(
          '%(counter)s result',
          '%(counter)s results',
      len(data)) % {
          'counter': len(data),
      }
      #print data
      #data.insert(0, {"value":None,"label":label})
      return HttpResponse(dumps(data), mimetype='application/javascript')
          
  data = [{"value":None,"label":_("Server error")}]
  return HttpResponse(dumps(data), mimetype='application/javascript')