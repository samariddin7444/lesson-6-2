from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi developers")


def about(request):
    return HttpResponse("We are developed")
