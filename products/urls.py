from django.urls import path

from products.views import ProductsListAPIView, ProductAPIView, CategoryListApiView, CategoryAPIView

urlpatterns = [
    path('products/', ProductsListAPIView.as_view()),
    path('products/<int:pk>/', ProductAPIView.as_view()),
    path('categories/', CategoryListApiView.as_view()),
    path('categories/<int:pk>/', CategoryAPIView.as_view()),
]