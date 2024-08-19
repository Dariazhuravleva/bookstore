from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Books
from .serializers import BooksSerializer


def index(request):
    return HttpResponse('Application books')


def genres(request, genre):
    return HttpResponse('All genres')


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


# class BooksAPIView(generics.ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
#
#
# class BooksAPIUpdate(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
#
#
# class BooksAPIViews(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
