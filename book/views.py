from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

books = [
    {"id":1, "name":"The Blind Owl", "writer":"Sadegh Hedayat"},
    {"id":2, "name":"The School Principal", "writer":"Jalal Al-e Ahmad"},
    {"id":3, "name":"Savushun", "writer":"Simin Daneshvar"},
    {"id":4, "name":"I'll Turn Off the Lights", "writer":"Zoya Pirzad"},
    {"id":5, "name":"Kelidar", "writer":"Mahmoud Dowlatabadi"},
    {"id":6, "name":"Symphony of the Dead", "writer":"Abbas Maroufi"},
    {"id":7, "name":"The Empty Place of Soluch", "writer":"Mahmoud Dowlatabadi"},
    {"id":8, "name":"Forty Short Letters to My Wife", "writer":"Nader Ebrahimi"},
]

def book_list (request):
    data = ''.join(f"id: {item['id']} , name: {item['name']} , writer: {item['writer']}<br>" for item in books)
    return HttpResponse(data)

def standard_book_list (request):
    return render(request,"book/list.html" , context={"books":books})

def detail (request):
    return HttpResponse('book detial!')