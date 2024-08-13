from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Application books')


def genres(request, genre):
    return HttpResponse('All genres')


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')
