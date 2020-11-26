from django.db import models
from datetime import date 
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class Restaurant(models.Model):
    name          = models.CharField(max_length=300)
    street        = models.CharField(max_length=300)
    city          = models.CharField(max_length=100, default='Dhaka')
    district      = models.CharField(max_length=100, default='Dhaka')
    country       = models.CharField(max_length=100, default='Bangladesh')
    telephone     = models.CharField(max_length=100, blank=True, null=True)
    url           = models.URLField(max_length=200, blank=True, null=True)
    date          = models.DateField(default=date.today)
    image         = models.ImageField()
    user          = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant-detail', kwargs={'pk': self.pk})



class Dish(models.Model):
    name         = models.CharField(max_length=200)
    description  = models.TextField()
    price        = models.DecimalField(max_digits=8, decimal_places=2)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    date         = models.DateField(default=date.today)
    image        = models.ImageField(blank=True, null=True)
    restaurant   = models.ForeignKey(Restaurant, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dishes-detail', kwargs={
            'pkr': self.restaurant.id,
            'pk': self.id
        })



class Review(models.Model):
    RATING_CHOICES    = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating            = models.PositiveSmallIntegerField('Rating Stars', blank=False, default=3,choices=RATING_CHOICES)
    comment           = models.TextField()
    user              = models.ForeignKey(User, on_delete=models.CASCADE)
    date              = models.DateField(default=date.today)

    class Meta:
        abstract = True



class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
