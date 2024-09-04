from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def data(request):
    return HttpResponse("<h1>Страница data моего проекта Джанго</h1>")

def test(request):
    return HttpResponse("<h1>Страница test моего проекта Джанго</h1>")
