from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from.models import Book
from django.urls import reverse,reverse_lazy

class ListBookView(ListView):
    template_name='book/Diary.html'
    model=Book 
    # object_list = Book.objects.order_by('id')
    # return render(request, 'book/Diary.html', {'object_list':object_list})

class DetailBookView(DetailView):
    template_name='book/book_detail.html'
    model=Book

class Toukou(CreateView):
    template_name = 'book/toukou.html'
    model = Book
    fields = ('title','text')
    success_url = reverse_lazy('list-book')
