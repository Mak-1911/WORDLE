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
    if(int(key) == 200):
        p.score += 200
    elif(int(key) == 0):
        p.score += 0
    p.game += 1
    p.save()
    return redirect('play')

def leaderboard(request):
    p = Profile.objects.all()
    return render(request,'leaderboard.html',{'p':p})