from rest_framework import serializers

from .models import Movie
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model=Movie
        fields='__all__'

        # fields = ['id','movie_name','director']


class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model=Movie
        fields='__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Movie
        fields='__all__'


        