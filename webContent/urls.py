from django.urls import path

from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('clothing', views.clothing, name='clothing'),
    path('contact', views.contact, name='contact'),
    path('essay', views.essay, name='essay'),
    path('gallery', views.gallery, name='gallery'),
    path('home', views.home, name='home')
]
