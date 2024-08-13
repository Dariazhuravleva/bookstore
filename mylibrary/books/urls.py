from django.urls import path
from books import views

urlpatterns = [
    path('',  views.index, name='home'),
    path('genres/<slug:genre>', views.genres, name='genres'),
]