from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Мой проект Джанго</h1>")

def new(request):
    return HttpResponse("<h1>Вторая страница моего проекта Джанго</h1>")
