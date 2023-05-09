from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
import datetime
def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('hello 00;))')


def youtube(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com/')



def google(request):
    if request.method == 'GET':
        return redirect('https://www.google.com/')


def git(request):
    if request.method == 'GET':
        return redirect('https://github.com/')

def now_date(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        return HttpResponse(now.strftime("%Y-%m-%d %H:%M:%S"))

def goodby(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")


