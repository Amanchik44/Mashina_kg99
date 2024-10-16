from django_filters import FilterSet
from .models import Car,Model


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'price': ['gt','lt'],
            'category': ['exact'],
            'car_name': ['exact'],

         }


class ModelFilter(FilterSet):
    class Meta:
        model = Model
        fields = {
           'model_name':['exact']

        }