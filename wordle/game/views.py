from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    return render(request, 'index.html')

def play(request):
    user = User.objects.get(username = request.user)
    p = Profile.objects.get(user = user)
    return render(request,'play.html',{'p':p})

def logout_view(request):
    logout(request)
    return render(request,'index.html',{})    

def wordlegame(request):
    user = User.objects.get(username = request.user)
    return render(request,'wordlegame.html',{})

def play2(request,key):
    user = User.objects.get(username = request.user)
    p = Profile.objects.get(user = user)
    if(int(key) == 60):
        p.score += 60
    elif(int(key) == 30):
        p.score += 30
    elif(int(key) == 20):
        p.score += 20
    elif(int(key) == 15):
        p.score += 15
    elif(int(key) == 12):
        p.score += 12            
    elif(int(key) == 0):
        p.score += 0
    p.game += 1
    p.save()
    return redirect('play')

def leaderboard(request):
    p = Profile.objects.all()
    return render(request,'leaderboard.html',{'p':p})

def choosetheme(request):
    user = User.objects.get(username = request.user)
    p = Profile.objects.get(user = user)
    return render(request,'choosetheme.html',{'p':p})

def chooseone(request):
    user = User.objects.get(username = request.user)
    p = Profile.objects.get(user = user)
    if request.method == 'POST':
        theme = request.post['theme']
        data = Profile(theme=theme)
        data.save()
        if theme == 'Automobile':
            Words = ["steer","brake","wheel","shaft","motor","speed","crank","screw"]