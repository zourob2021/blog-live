import django_filters
from django_filters import DateFilter,CharFilter
from .models import *

class orderfilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='datum_create',lookup_expr='gte')
    end_date = DateFilter(field_name='datum_create',lookup_expr='lte')
    note =  CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = order
        fields = '__all__'
        exclude = ['customer','datum_create ']

