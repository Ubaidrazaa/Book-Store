from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg
from .models import book
# Create your views here.
def index(request):
    books = book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request,"book/index.html",{
        "books": books,
        "total_no_of_books": num_books,
        "average_rating": avg_rating,
    })

def book_detail(request, slug):
    #try:
    #    Book = book.objects.get(pk=id)
    #except:
    #    raise Http404()
    Book = get_object_or_404(book, slug=slug)
    return render(request,"book/book_detail.html",{
        "title": Book.title,
        "author": Book.author,
        "rating": Book.rating,
        "is_bestseller": Book.is_bestselling,
    })