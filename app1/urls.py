from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    # path("add", views.add, name='add'),
    path("services", views.services, name='dictionary'),
    path("search", views.search, name='search'),
]