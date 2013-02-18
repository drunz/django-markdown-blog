from django.views.generic import ListView
from blog.models import Post
from django.views.generic.edit import BaseCreateView

class TagArchiveListView(ListView):
    def get_queryset(self):
        tag_slug = self.args[0]
        return Post.objects.filter(tags__slug=tag_slug).order_by('-date')

class ListCreateView(ListView, BaseCreateView):
    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(ListCreateView, self).get_context_data(**kwargs)
        return context

"""
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Post

# Template url: {% url blog.views.index %}
def index(request):
    posts = Post.objects.order_by('-date')
    return render_to_response('blog.html', {'posts': posts},
                              context_instance=RequestContext(request))
"""
