from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, CreateView, ArchiveIndexView, DetailView
from blog.models import Post
from blog.views import ListCreateView, TagArchiveListView

urlpatterns = patterns('',  
    #url(r'^$', 'blog.views.index'),
    # List view for posts
    url(r'^$', ListView.as_view(
        queryset=Post.objects.order_by('-date'),
        context_object_name="posts",
        template_name='blog.html',
        paginate_by=5,
    ), name="blog-index"),
    # Index view for post archive
    url(r'^archive/$', ArchiveIndexView.as_view(
        model=Post,
        date_field='date',
        template_name='archive.html',
        paginate_by=20,
    ), name="blog-archive"),
    # Detail view for post
    url(r'^post/(?P<slug>[-\w]+)/$', DetailView.as_view( 
        model=Post,
        template_name='detail.html',
    ), name="blog-detail"),
    # List view for tag archive
    url(r'^archive/([-\w]+)/$', TagArchiveListView.as_view(
        context_object_name="latest",
        template_name="archive.html",
        paginate_by=5,
    ), name="blog-tagarchive"),
    # Search urls
    url(r'^search/', include('haystack.urls'),
        name="blog-search"
    ),

    # ***** T E S T I N G *****

    # Combined list and create view for posts
    url(r'^mixed/$', ListCreateView.as_view(
        queryset=Post.objects.order_by('-date'),
        #context_object_name="posts",
        template_name='mixed.html',
        success_url='/landing/blog/post/%(slug)s/',
    )),
    # Create view modal for post
    url(r'^create/$', CreateView.as_view(
        model=Post,
        template_name='mixed.html',
        success_url='/post/%(slug)s/',
    )),
)
