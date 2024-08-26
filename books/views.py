from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import book
# Create your views here.
def index(request):
    books = book.objects.all()
    return render(request,"book/index.html",{
        "books": books
    })

def book_detail(request, id):
    #try:
    #    Book = book.objects.get(pk=id)
    #except:
    #    raise Http404()
    Book = get_object_or_404(book, pk=id)
    return render(request,"book/book_detail.html",{
        "title": Book.title,
        "author": Book.author,
        "rating": Book.rating,
        "is_bestseller": Book.is_bestselling,
    })