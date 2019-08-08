from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # no .as_view() since its just a function
    path('books/', views.BookListView.as_view(), name='books'), # include .as_view() since class-based
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),  # <int:pk> captures the specific id of the book
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]