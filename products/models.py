from django.db import models

from users.models import CustomUser


class Category(models.Model):
    """Категория товаров"""
    title = models.CharField('Название категории', max_length=155)
    description = models.TextField('Описание категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class Products(models.Model):
    """Товары"""
    title = models.CharField('Название товара', max_length=155)
    description = models.TextField('Описание товаров')
    price = models.DecimalField('Цена товара', max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_status = models.BooleanField('Тип')
    categ = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='categories')
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='users', default=1)
