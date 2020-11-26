from django.urls import path, include
from .views import RestaurantDetailView, RestaurantCreateView, RestaurantUpdateView, DishesCreateView, DishesDetailView, DishesUpdateView, review



urlpatterns = [
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant-edit'),
    path('<int:pk>/dishes/create/', DishesCreateView.as_view(), name='dishes-create'),
    path('<int:pkr>/dishes/<int:pk>', DishesDetailView.as_view(), name='dishes-detail'),
    path('<int:pkr>/dishes/<int:pk>/edit', DishesUpdateView.as_view(), name='dishes-edit'),
    path('<int:pk>/reviews/create', review, name='review-create'),
]

