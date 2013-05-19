from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^authors$', views.listAllAuthors, name='listAllAuthors'),
    url(r'^authors/new$', views.createAuthor, name='createAuthor'),
    url(r'^authors/detail$', views.listAuthor, name='listAuthor'),
)
