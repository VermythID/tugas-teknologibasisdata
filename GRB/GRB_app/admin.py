from django.contrib import admin
from .models import BookCategory, Books, Publishers, Stores

# Register your models here.
admin.site.register(BookCategory)
admin.site.register(Books)
admin.site.register(Publishers)
admin.site.register(Stores)