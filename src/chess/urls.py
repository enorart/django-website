from django.urls import path

from .views import index, info

urlpatterns = [
    path('',index, name="chess-index"),
    path('info/',info,name="chess-info"),
]