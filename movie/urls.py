from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.movie_list,name='list'),
    path('<int:pk>/',views.MovieDetail.as_view(),name='detail'),

]
