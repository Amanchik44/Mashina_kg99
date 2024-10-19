from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'phone_number', 'first_name', 'last_name', 'age']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,


            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),



        }


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')


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


class CarListSerializers(serializers.ModelSerializer):
    # model = ModelSerializers()
    # add_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S ')
    # car_make = CarMakeSerializers()
    # category = CategorySerializers()

    class Meta:
        model = Car
        fields = ['car_name','car_make','model','year','price',
                  'city','with_photo'
                  ]


class CarDetailSerializers(serializers.ModelSerializer):
    model = ModelSerializers()
    car_make = CarMakeSerializers()
    category = CategorySerializers()
    add_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S ')

    class Meta:
        model = Car
        fields = ['car_name','category','car_make','model','description','year','price',
                  'city','color_car','country','mileage','with_photo','drive','engine',
                  'volume','exchange','steering_wheel','add_date']






