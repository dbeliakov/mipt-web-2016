from django.conf.urls import url

from forum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
    url(r'^thread/(?P<thread_id>\d+)/(?P<page_num>\d+)/$', views.thread, name='thread'),
    url(r'^profile/(?P<profile_id>\d+)/$', views.profile, name='profile'),

]
