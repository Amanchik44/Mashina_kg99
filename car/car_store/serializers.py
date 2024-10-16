from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CarMakeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['car_make_name']


class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_name']


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteCarSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCar
        fields = '__all__'


class CarSerializers(serializers.ModelSerializer):
    model = ModelSerializers()
    car_make = CarMakeSerializers()
    category = CategorySerializers()
    add_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S ')

    class Meta:
        model = Car
        fields = ['car_name','category','car_make','model','description','year','price',
                  'city','color_car','country','mileage','with_photo','drive','engine',
                  'volume','exchange','steering_wheel','add_date']






