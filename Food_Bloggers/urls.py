from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from .views import HomeListView, RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeListView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),       #no views only TEMPLATE needed
    path('logout/', LogoutView.as_view(), name='logout'),    #no VIEWS no template needed
    path('register/', RegisterUserView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  #Used for password reset url only
    #local_apps goes here ... 
    path('restaurant/', include('restaurantApp.urls')),
]
if settings.DEBUG: 
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)