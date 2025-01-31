from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

book_list = [
    {"id":1, "name":"book1", "writer":"Sadiq Hedayat"},
    {"id":2, "name":"book2", "writer":"Jalal Al Ahmad"},
    {"id":3, "name":"book3", "writer":"Simin Daneshwar"}
]

def books (request):
    data = ''.join(f"id: {item['id']} , name: {item['name']} , writer: {item['writer']}<br>" for item in book_list)
    return HttpResponse(data)

def detail (request):
    return HttpResponse('book detial!')