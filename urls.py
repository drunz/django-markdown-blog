from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'quotes.views.index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pagelets-management/', include('pagelets.urls.management')),
    url(r'^page/', include('pagelets.urls.content')),

    # Examples:
    # url(r'^$', 'landing.views.home', name='home'),
    # url(r'^landing/', include('landing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^grappelli/', include('grappelli.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
