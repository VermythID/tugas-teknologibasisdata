from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.views import View
from .models import BookCategory, Books, Publishers, Stores

# Create your views here.

def view_stores(request):
    stores = Stores.objects.all().order_by('store_id')
    return render(request, 'stores.html',
                  {
                      'stores': stores
                  })
def dml_stores(request):
    if request.method == "POST":
        address = request.POST['address']
        district = request.POST['district']
        city_id = request.POST['city_id']
        postal_code = request.POST['postal_code']
        phone = request.POST['phone']

        data = Stores(address = address, district = district, city_id = city_id, postal_code = postal_code, phone = phone)
        data.save()

        return redirect('/')
    return render(request, 'add_store.html')

def edit_stores(request, pk):
    stores = Stores.objects.get(store_id = pk)
    if request.method == "POST":
        stores.address = request.POST.get('address')
        stores.district = request.POST.get('district')
        stores.city_id = request.POST.get('city_id')
        stores.postal_code = request.POST.get('postal_code')
        stores.phone = request.POST.get('phone')
        stores.save()
        return redirect('/')

    context = {
        'stores': stores,
    }
    return render(request, 'edit_store.html', context)

def remove_store(request, pk):
    stores = Stores.objects.get(store_id = pk)
    books = Books.objects.filter(store_id = stores)
    if request.method == "POST":
        books.all().delete()
        stores.delete()
        return redirect('/')

    context = {
        'stores': stores,
    }

    return render(request, 'delete_store.html', context)

@require_http_methods(["GET", "POST"])
def view_books(request):
    if request.method == "POST":
        store_id = request.POST.get('store_id')
        store = get_object_or_404(Stores, store_id = store_id)
        books = Books.objects.filter(store_id = store)

        return render(request, 'books.html',
                    {
                        'books': books,
                        'store_id': store_id,
                    })

def dml_books(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        release_year = request.POST['release_year']
        languages = request.POST['languages']
        store_id = request.POST['store_id']
        publisher_id = request.POST['publisher_id']
        price = request.POST['price']

        data = Books(
                title = title,
                description = description, 
                release_year = release_year, 
                languages = languages, 
                store_id = store_id,
                publisher_id = publisher_id,
                price = price,
            )
        data.save()

        return redirect('/')
    return render(request, 'add_book.html')

def edit_books(request, pk):
    books = Books.objects.get(book_id = pk)
    if request.method == "POST":
        books.title = request.POST['title']
        books.description = request.POST['description']
        books.release_year = request.POST['release_year']
        books.languages = request.POST['languages']
        books.store_id = request.POST['store_id']
        books.publisher_id = request.POST['publisher_id']
        books.price = request.POST['price']
        books.save()
        return redirect('/')

    context = {
        'books': books,
    }
    return render(request, 'edit_book.html', context)

def remove_book(request, pk):
    books = Books.objects.get(book_id = pk)
    if request.method == "POST":
        books.delete()
        return redirect('/')

    context = {
        'books': books,
    }

    return render(request, 'delete_book.html', context)