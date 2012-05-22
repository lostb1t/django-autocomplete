django-autocomplete
================

This app extends **django-taggit** with an autocomplete field provided by the awesome **jQuery's TextExt plugin** (http://textextjs.com/).

Using it
--------

1. Add to `settings.py`:

        INSTALLED_APPS = (
            # ...
            'autocomplete',
        )
        
2. Add to URLs:

        url(r'^admin/autocomplete/', include('autocomplete')),

3. Add to your models:

        from django.db import models
        from autocomplete.managers import TaggableManager
        
        class Page(models.Model):
            # ...
            tags = TaggableManager()

5. If you want to use autocomplete field out of the admin make sure you make the the grappelli jquery namespace avaible in your template

        var django = {
          "jQuery": jQuery.noConflict()
        };

5. Enjoy a sane tagging widget on the admin

This package includes a slightly modified copy of the TextExt plugin to work smooth with Grappelli, but you can serve your own by setting `AUTOCOMPLETE_JS_PATH` on `settings.py`.

This app is based off: https://github.com/hcarvalhoalves/django-taggitext