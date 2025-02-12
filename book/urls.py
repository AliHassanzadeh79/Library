from django.urls import path
from . import views

urlpatterns = [
    path('list', views.book_list),
    path('standard-list', views.standard_book_list),
    path('detail', views.detail),
]