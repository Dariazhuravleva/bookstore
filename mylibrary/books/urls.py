from django.urls import path, include
from books import views
from books.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('',  views.index, name='home'),
    path('genres/<slug:genre>', views.genres, name='genres'),
    path('api/v1/', include(router.urls)),
]
