from django.shortcuts import render, get_object_or_404
import requests
import urllib, json
# Create your views here.


def dlivelay_index(request):
    if request.method == 'POST':
        username = request.POST.get("name", "")
        url = "https://api.steemjs.com/get_discussions_by_author_before_date?author="+username+"&beforeDate=2016-07-23T22%3A00%3A06&limit=50"
        data = requests.get(url)
        posts=data.json()
        newdict=[]
        for post in posts:
            if post['category']=='dlive':
                newdict.append({post['title']:post['permlink']})
                break
        return render(request, 'dlivelay/index.html',{'posts': newdict, 'author': post['author']})
    else:
        return render(request, 'dlivelay/index.html')


def chat(request, username, permlink):
    return render(request, 'dlivelay/chat.html', {'username': username, 'permlink': permlink})


def follower_count(request, username):
    return render(request, 'dlivelay/follower.html', {'username':username})

def follower_goal(request, username, goal):
    return render(request, 'dlivelay/followergoal.html', {'username':username,'goal':goal})

def upvoter(request, username, permlink):
    return render(request, 'dlivelay/upvoter.html', {'username':username, 'permlink':permlink})