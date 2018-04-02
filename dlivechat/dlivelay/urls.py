from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.dlivelay_index, name='index'),
    path('fcount/<username>/', views.follower_count, name='fcount'),
    path('fgoal/<username>/<goal>/', views.follower_goal, name='fcount'),
    path('chat/<username>/<permlink>/', views.chat, name='chat'),
    path('upvote/<username>/<permlink>/', views.upvoter, name='chat'),
]