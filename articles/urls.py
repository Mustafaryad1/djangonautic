from django.conf.urls import url
from . import views

app_name = 'articles'
urlpatterns = [

    url(r'^$', views.article_list, name='list'),
    url(r'^create/$', views.article_create, name='create'),
    url(r'^user/(?P<author>[\w]+)/$', views.user_articles, name='user_articles'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_details, name='details'),
    # url(r'^(?P<author>[0-9]+)/$', views.user_articles, name='user_articles'),
]
