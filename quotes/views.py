from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.cache import cache_page
from django.template import RequestContext
from quotes.models import Quote

@cache_page(60 * 60 * 24) # 24h
def index(request):
    quotes = Quote.objects.all()
    return render_to_response('index.html', {'quotes': quotes},
                              context_instance=RequestContext(request))
