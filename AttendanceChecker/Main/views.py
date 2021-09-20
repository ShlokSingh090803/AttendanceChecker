from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from django.conf import settings

# Create your views here.
def index(response):
    return render(response,"Main\home.html")