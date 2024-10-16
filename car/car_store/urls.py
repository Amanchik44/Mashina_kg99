from django.urls import path
from .views import *


urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),

    path('', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_list'),
    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve',
                                          'put': 'update',
                                          'delete': 'destroy'}), name='car_detail'),

    path('user', UserProfileViewSet.as_view({'get': 'list',}), name='movie_list'),
    path('user<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'}), name='movie_detail'),

    path('category', CategoryViewSet.as_view({'get': 'list', }), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'}), name='category_detail'),

    path('car_make', CarMakeViewSet.as_view({'get': 'list'}), name='car_make_list'),
    path('car_make/<int:pk>/', CarMakeViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'}), name='car_make_detail'),


    path('model', ModelViewSet.as_view({'get': 'list'}), name='model_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'}), name='model_detail'),



    path('comment', CommentViewSet.as_view({'get': 'list'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'}), name='comment_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorite_detail'),

    path('favorite_movie/', FavoriteCarViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='favorite_movie_list'),
    path('favorite_movie/<int:pk>/',
         FavoriteCarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorite_movie_detail'),



]
