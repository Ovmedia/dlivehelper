from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path('index/', views.dlivelay_index, name='index'),
    path('', views.login, name='main'),
    path('fcount/<username>/', views.follower_count, name='fcount'),
    path('fgoal/<username>/<goal>/', views.follower_goal, name='fcount'),
    path('chat/<username>/<permlink>/', views.chat, name='chat'),
    path('upvote/<username>/<permlink>/', views.upvoter, name='chat'),
]