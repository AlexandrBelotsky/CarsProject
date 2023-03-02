from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from post.forms import FCars
from post.models import Cars, Category


def index(request):
    cars = Cars.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'post/cars_menu.html', context)

def show_info(request, info_slug):
    cars_info = Cars.objects.filter(slug=info_slug)
    current_cars_info = Cars.objects.get(slug=info_slug)

    context = {
        'cars_info': cars_info,
        'current_cars_info': current_cars_info,

    }
    return render(request, 'post/cars_info.html', context)


def show_category(request, cars_slug):
    cars = Cars.objects.filter(category__slug=cars_slug)
    current_cats = Category.objects.get(slug=cars_slug)
    context = {
        'cars': cars,
        'current_cats': current_cats
    }
    return render(request, 'post/cars_category.html', context)




class CreateCars(CreateView):
    template_name = 'post/create.html'
    form_class = FCars
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
#







