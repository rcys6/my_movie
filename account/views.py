from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from movie.models import Movie
from movie.serializers import MovieSerializer
from account.models import Profile
# Create your views here.

class CollectViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

    # 展示以及收藏
    def list(self,request):
        user=request.user
        profile=Profile.objects.get(user=user)
        movie=profile.movies.all()
        serializer=MovieSerializer(movie,many=True)
        return Response(serializer.data)

    def create(self,request):
        user=request.user
        profile=Profile.objects.get(user=user)
        movie_id=request.data['movie_id']
        try:
            movie=Movie.objects.get(id=movie_id)
            profile.movies.add(movie)
            return Response ({'message':'收藏成功'})
        except ObjectDoesNotExist:
            return Response({'message':'电影信息不存在'})
        except:
            return Response({'message':'收藏失败'})

    def destroy(self, request,pk):
        user=request.user
        profile=Profile.objects.get(user=user)
        try:
            movie=Movie.objects.get(id=pk)
            if movie not in profile.movies.all():
                return Response({'message':'未收藏该电影'})
            profile.movies.remove(movie)
            return Response ({'message':'取消收藏成功'})
        except ObjectDoesNotExist:
            return Response({'message':'电影信息不存在'})
        except:
            return Response({'message':'取消收藏失败'})
        
    # detail设置单一资源的
    @action(detail=True,methods=['get']) # 自主定义接口
    def is_collected(self,request,pk=None):
        user=request.user
        profile=Profile.objects.get(user=user)
        movie=Movie.objects.get(id=pk)
        is_collected=profile.movies.filter(id=movie.id).exists()
        return Response({'is_collected':is_collected})
