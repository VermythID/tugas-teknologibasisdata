from django.urls import path
from . import views

app_name = 'GRB_app'

urlpatterns = [
    ## Main Page
    path('', views.view_stores, name = 'view_stores'),
    ## Add Store from Store List (from Main Page)
    path('dml_stores/', views.dml_stores, name = 'dml_stores'),
    ## Manipulate selected store's attributes (from Store Detail page)
    path('edit_stores/<int:pk>', views.edit_stores, name = 'edit_stores'),
    path('remove_store/<int:pk>', views.remove_store, name = 'remove_store'),

    ## View all the books from selected store
    path('books/', views.view_books, name = 'view_books'),

    ## Add Books from Book List (from selected store's page)
    path('dml_books/', views.dml_books, name = 'dml_books'),
    ## Manipulate selected book's attributes
    path('edit_books/<int:pk>', views.edit_books, name = 'edit_books'),
    path('remove_book/<int:pk>', views.remove_book, name = 'remove_book'),
]