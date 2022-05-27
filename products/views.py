from django.shortcuts import render
from django.http import HttpResponse, Http404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Products, Category
from products.serializers import ProductSerializer, CategorySerializer
from users.models import CustomUser


class ProductsListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['categ', 'is_status']
    search_fields = ['title', 'price', 'created_at']
    ordering_fields = ['user', ]

    @swagger_auto_schema(
        operation_summary='Get list of products',
        responses={
            '200': ProductSerializer(many=True),
        },
    )
    def get(self, request):
        try:
            products_qs = Products.objects.select_related('categ').select_related('user').all()
        except Products.DoesNotExist:
            raise Http404
        product_srz = ProductSerializer(products_qs, many=True)
        return Response(product_srz.data, status=status.HTTP_200_OK)


class CategoryListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_summary='Get list of categories',
        responses={
            '200': ProductSerializer(many=True),
        },
    )
    def get(self, request):
        try:
            categ_qs = Category.objects.all()
        except Category.DoesNotExist:
            raise Http404
        category_srz = CategorySerializer(categ_qs, many=True)
        return Response(category_srz.data, status=status.HTTP_200_OK)


class CategoryAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_summary='Get detail of categories',
        responses={
            '200': CategorySerializer(many=False),
            '404': 'Category not found.',
        }
    )
    def get(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
        category_srz = CategorySerializer(category, many=False)
        return Response(category_srz.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Create a product',
        request_body=ProductSerializer(many=False),
        responses={
            '201': ProductSerializer(many=False),
        },
    )
    def post(self, request):
        body = request.data
        category = Category.objects.create(title=body['title'], description=body['description'])
        category_srz = CategorySerializer(category, many=False)
        return Response(category_srz.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Delete category',
        request_body=None,
        responses={'204': None}
    )
    def delete(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_summary='Update detail of category',
        responses={
            '200': ProductSerializer(many=False),
        },
        request_body=ProductSerializer(many=False)
    )
    def put(self, request, pk):
        body = request.data
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404
        category.title = body['title']
        category.description = body['description']
        category.save()

        category_srz = CategorySerializer(category, many=False)
        return Response(category_srz.data, status=status.HTTP_200_OK)


class ProductAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_summary='Get detail of product',
        responses={
            '200': ProductSerializer(many=False),
            '404': 'Product not found.',
        }
    )
    def get(self, request, pk):
        try:
            products = Products.objects.get(id=pk)
        except Products.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        product_srz = ProductSerializer(products, many=False)
        return Response(product_srz.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Create a product',
        request_body=ProductSerializer(many=False),
        responses={
            '201': ProductSerializer(many=False),
        },
    )
    def post(self, request):
        body = request.data
        product = Products.objects.create(
            title=body['title'], description=body['description'],
            price=body['price'], is_status=body['is_status'],
            categ=body['categ'], user=body['user'],
        )
        product_srz = ProductSerializer(product, many=False)
        return Response(product_srz.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Delete a product',
        request_body=None,
        responses={'204': None}
    )
    def delete(self, request, pk):
        try:
            product = Products.objects.get(id=pk)
        except Products.DoesNotExist:
            return Response({'message': 'Todo not found.'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_summary='Update detail of product',
        responses={
            '200': ProductSerializer(many=False),
        },
        request_body=ProductSerializer(many=False)
    )
    def put(self, request, pk):
        body = request.data
        try:
            product = Products.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404
        product.title = body['title']
        product.description = body['description']
        product.price = body['price']
        product.is_status = body['is_status']
        product.categ = body['categ']
        product.user = body['user']
        product.save()

        todo_srz = ProductSerializer(product, many=False)
        return Response(todo_srz.data, status=status.HTTP_200_OK)
