from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from restaurantApp.models import Restaurant, Dish, RestaurantReview
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegisterUserForm
from django.http import HttpResponseForbidden, HttpResponse
from django.db.models import Q
# Create your views here.


class HomeListView(ListView):
    model = Restaurant
    template_name = 'home_list.html'
    context_object_name = 'restaurant_list'
    paginate_by = 6
    queryset = Restaurant.objects.order_by('-id')

    def get_queryset(self):
        result = super().get_queryset()
        search = self.request.GET.get('q')

        if search:
            result = result.filter(
                Q(name__icontains=search)
            )
        return result 



class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden()
        
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        #return HttpResponse('User Registered')
        return redirect('login')
