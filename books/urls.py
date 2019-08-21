from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    path('books/add/', views.BookCreate.as_view(), name='book_add'),
]