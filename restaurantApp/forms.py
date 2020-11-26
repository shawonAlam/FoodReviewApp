from django import forms
from .models import Restaurant, Dish

class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        exclude = ['user', 'date',]

class DishesForm(forms.ModelForm):

    class Meta:
        model = Dish
        exclude = ['user', 'date', 'restaurant',]