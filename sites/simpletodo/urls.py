from django.conf.urls.defaults import patterns, url
from simpletodo import views

urlpatterns = patterns('',
    url('^todo/$', views.index, name='todo_idx'),
    url('^todo/new/$', views.new, name='todo_new'),
    url('^todo/(?P<id>\d+)/edit/$', views.edit, name='todo_edit'),
    url('^todo/(?P<id>\d+)/delete/$', views.delete, name='todo_delete'),
    url('^todo/(?P<id>\d+)/finish/$', views.finish, name='todo_finish'),
)
