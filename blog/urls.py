from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^authors$', views.listAllAuthors, name='listAllAuthors'),
    url(r'^authors/detail$', views.listAuthor, name='listAuthor'),
    url(r'^authors/new$', views.createAuthor, name='createAuthor'),
    url(r'^posts$', views.listAllPosts, name='listAllPosts'),
    url(r'^posts/detail$', views.listPost, name='listPost'),
    url(r'^posts/new$', views.createPost, name='createPost'),
    url(r'^posts/delete$', views.deletePost, name='deletePost'),
    url(r'^posts/modify$', views.modifyPost, name='modifyPost'),
)
