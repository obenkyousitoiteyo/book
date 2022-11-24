from django.shortcuts import render
from django.views.generic import ListView,DetailView
from.models import Book

class ListBookView(ListView):
    template_name='book/Diary.html'
    model=Book 

class DetailBookView(DetailView):
    template_name='book/book_detail.html'
    model=Book
# Create your views here.
