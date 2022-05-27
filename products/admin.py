from django.contrib import admin

from products.models import Category, Products
from users.models import Gender, CustomUser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender']

    def has_add_permission(self, request):
        gender_count = Gender.objects.all().count()
        if gender_count >= 2:
            return False
        else:
            return True


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
