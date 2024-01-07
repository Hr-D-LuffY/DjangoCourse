from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('categories/<slug:brand_slug>/', views.home, name='categorywise'),
    path('book/<int:id>/', views.bookdetails, name='bookDetails'),
    path('borrow/book/<int:id>/', views.borrowBook, name='borrowBook'),
    path('return/book/<int:id>/', views.returnBook, name='returnBook'),
    path('user/', include('user.urls')),
]