from django.conf.urls import url

from lessons import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lessons/(?P<lesson_id>\d+)/$', views.lesson, name='lesson'),
    url(r'^problems/(?P<problem_id>\d+)/$', views.problem, name='problem'),
    url(r'^send_submission/(?P<problem_id>\d+)/$', views.send_submission, name='send_submission'),
]
