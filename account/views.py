from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from movie.models import Movie
from movie.serializers import MovieSerializer

from account.models import Profile
# Create your views here.

class CollectViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

    # 展示以及收藏
    def list(self,request):
        pass

    def create(self,request):
        user=request.user
        profile=Profile.objects.get(user=user)
        moive_id=request.data['movie_id']
        movie=Movie.objects.get(id=moive_id)
        profile.movies.add(movie)
        return Response ({'message':'收藏成功'})


