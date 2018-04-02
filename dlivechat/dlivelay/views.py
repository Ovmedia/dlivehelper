from django.shortcuts import render, get_object_or_404
import requests
import urllib, json
# Create your views here.


def dlivelay_index(request):
    return render(request, 'dlivelay/index.html')

def base(request):

    return render(request, 'dlivelay/user.html')


def chat(request, username, permlink):
    return render(request, 'dlivelay/chat.html', {'username': username, 'permlink': permlink})


def follower_count(request, username):
    return render(request, 'dlivelay/follower.html', {'username':username})

def follower_goal(request, username, goal):
    return render(request, 'dlivelay/followergoal.html', {'username':username,'goal':goal})

def upvoter(request, username, permlink):
    return render(request, 'dlivelay/upvoter.html', {'username':username, 'permlink':permlink})

def old_login(request):
    if request.method == 'POST':
        username = request.POST.get("find", "")
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

def login(request):
    if request.method == 'POST':
        username = request.POST.get("find", "")
        url = "https://api.steemjs.com/get_discussions_by_author_before_date?author="+username+"&beforeDate=2016-07-23T22%3A00%3A06&limit=50"
        data = requests.get(url)
        posts=data.json()
        newdict=[]
        sayac=0
        for post in posts:
            if post['category']=='dlive':
                newdict.append({post['title']:post['permlink']})
                sayac=sayac+1
                if (sayac==3):
                    break
        url = "https://api.steemjs.com/get_accounts?names[]=%5B%22"+username+"%22%5D"
        data = requests.get(url)
        profile = data.json()
        print(profile)
        profile_sbd=profile[0]['sbd_balance']
        profile_steem=profile[0]['balance']
        profile_meta = json.loads(profile[0]['json_metadata'])
        profile_name=profile[0]['name']
        url = "https://api.steemjs.com/get_follow_count?account="+username
        data = requests.get(url)
        fcount = data.json()
        fcount = fcount['follower_count']
        return render(request, 'dlivelay/user.html',{'posts': newdict,
                                                     'author': post['author'],
                                                     'profile_name':profile_name,
                                                     'profile_sbd':profile_sbd.split(" ")[0],
                                                     'profile_steem':profile_steem.split(" ")[0],
                                                     'fcount':fcount
                                                     })
    else:
        return render(request, 'dlivelay/main.html')