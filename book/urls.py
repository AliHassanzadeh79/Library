from django.urls import path
from . import views

urlpatterns = [
    path('list', views.books),
    path('detail', views.detail),
]