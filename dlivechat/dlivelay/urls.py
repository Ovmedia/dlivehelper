from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path('old/', views.old_login, name='oldlogin'),
    path('', views.login, name='main'),
    path('base/', views.base, name='base'),
    path('fcount/<username>/', views.follower_count, name='fcount'),
    path('fgoal/<username>/<goal>/', views.follower_goal, name='fcount'),
    path('chat/<username>/<permlink>/', views.chat, name='chat'),
    path('upvote/<username>/<permlink>/', views.upvoter, name='chat'),
    path('old/fcount/<username>/', views.follower_count, name='fcount'),
    path('old/fgoal/<username>/<goal>/', views.follower_goal, name='fcount'),
    path('old/chat/<username>/<permlink>/', views.chat, name='chat'),
    path('old/upvote/<username>/<permlink>/', views.upvoter, name='chat'),
]