from django.urls import path

from post.views import index, show_category, CreateCars, show_info

urlpatterns = [
    path('', index, name='index'),
    path('cars_info/<slug:info_slug>/', show_info, name='cars_info'),
    path('cars_category/<slug:cars_slug>/', show_category, name='cars_category'),
    path('create/', CreateCars.as_view(), name='create'),

]