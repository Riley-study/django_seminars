"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, cube, heads_or_tails, numbers, main_page, about_us, coin_values

urlpatterns = [
    path('', index, name='index'),
    path('heads_or_tails/', heads_or_tails, name='heads_or_tails'),
    path('cube/', cube, name='cube'),
    path('numbers/', numbers, name='numbers'),
    path('main/', main_page, name='main_page'),
    path('about_us/', about_us, name='about_us'),
    path('coin_values/', coin_values, name='coin_values'),
]
