from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Restaurant, Dish, RestaurantReview
from .forms import RestaurantForm, DishesForm
from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect

# Create your views here.



class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurantApp/restaurant_detail.html'
    context_object_name = 'restaurant_object'
    success_url = 'restaurant-detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context



class RestaurantCreateView(CreateView):
    model = Restaurant
    template_name = 'restaurantApp/restaurant_create.html'
    form_class = RestaurantForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        


class RestaurantUpdateView(UpdateView):
    model = Restaurant
    template_name = 'restaurantApp/restaurant_edit.html'
    form_class = RestaurantForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class DishesCreateView(CreateView):
    model = Dish
    template_name = 'restaurantApp/dishes_create.html'
    form_class = DishesForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class DishesDetailView(DetailView):
    model = Dish
    template_name = 'restaurantApp/dishes_detail.html'
    context_object_name = 'dishes_detail'



class DishesUpdateView(UpdateView):
    model = Dish
    template_name = 'restaurantApp/dishes_edit.html'
    form_class = DishesForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)



# class ReviewCreateView(CreateView):
#     success_url = 'restaurant-detail'

#     def get_queryset(self):
#         restaurant = get_object_or_404(Restaurant, pk=pk)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['review'] = RestaurantReview(
#             rating=request.POST['rating'],
#             comment=request.POST['comment'],
#             user=request.user,
#             restaurant=restaurant)
#         return context 



def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST.get('rating', False),
        comment=request.POST.get('comment', False),
        user=request.user,
        restaurant=restaurant
        )
    review.save()
    return HttpResponseRedirect(reverse('restaurant-detail', args=(restaurant.id,)))
