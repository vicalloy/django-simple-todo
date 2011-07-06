from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple_todo_site.views.home', name='home'),
    #url(r'^simple_todo_site/', include('simple_todo_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

from simpletodo import views

urlpatterns += patterns('',
    url('^$', views.index, name='todo_idx'),
    url('^todo/new/$', views.new, name='todo_new'),
    url('^todo/(?P<id>\d+)/edit/$', views.edit, name='todo_edit'),
    url('^todo/(?P<id>\d+)/delete/$', views.delete, name='todo_delete'),
    url('^todo/(?P<id>\d+)/finish/$', views.finish, name='todo_finish'),
)
