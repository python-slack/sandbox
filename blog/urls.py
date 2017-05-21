from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns=[
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='author_detail')
]