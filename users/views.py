from django.shortcuts import render
from django.http import HttpResponse


def users(request):
    return HttpResponse("Hello, world. You're at the")


def about(request):
    return HttpResponse("The best")
