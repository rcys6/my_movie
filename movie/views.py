from django.shortcuts import render
from django.http import JsonResponse,Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins,viewsets
from django_filters import rest_framework as filters
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser

from .serializers import MovieListSerializer,MovieDetailSerializer,MovieSerializer,CategorySerializer
from .models import Movie,Category
from .permision import IsAdminUserOrReadOnly

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=MovieListSerializer(movies,many=True)
#         return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#     elif request.method=='POST':

#         serializer=MovieListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# # 手动的
# class MovieDetailFiger(APIView):
#     # drf对象，主键
#     def get(self,request,pk):
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except:
#             raise Http404
        
#         serializer = MovieDetailSerializer(movie)
#         return Response(serializer.data)
    


#     def put(self,request,pk):
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except:
#             raise Http404
#         # partial部分更新
#         serializer = MovieDetailSerializer(movie,data=request.data,partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except:
#             raise Http404
        
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# /api/movie 接口
# 通用类
# class MovieDetail(generics.GenericAPIView,
#                   mixins.RetrieveModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.UpdateModelMixin):

#     queryset=Movie.objects.all()
#     serializer_class=MovieDetailSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     # 部分修改
#     def put(self,request,*args,**kwargs):
#         return self.partial_update(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

class MovieFilter(filters.FilterSet):
    movie_name=filters.CharFilter(lookup_expr='icontains')
    category_id=filters.NumberFilter()
    region=filters.NumberFilter()

    class Meta:
        model=Movie
        fields=['movie_name','category_id','region']


class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # 模糊查询
    filterset_class=MovieFilter
    permission_classes = [ IsAdminUserOrReadOnly ]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes = [ IsAdminUserOrReadOnly ]



