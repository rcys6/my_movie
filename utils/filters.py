from django_filters import rest_framework as filters
from movie.models import Movie
from trade.models import Order


class MovieFilter(filters.FilterSet):
    movie_name=filters.CharFilter(lookup_expr='icontains')
    category_id=filters.NumberFilter()
    region=filters.NumberFilter()

    class Meta:
        model=Movie
        fields=['movie_name','category_id','region']


class OrderFilter(filters.FilterSet):
    pay_status = filters.CharFilter(field_name='pay_status')
    order_sn = filters.CharFilter(field_name='order_sn')

    class Meta:
        model=Order
        fields=['order_sn','pay_status']