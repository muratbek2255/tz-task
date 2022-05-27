from datetime import datetime

from django.test import TestCase

from products.models import Category, Products
from users.models import CustomUser, Gender


class TestCategoryModel(TestCase):

    def test_create_category(self):
        category = Category.objects.create(title='first', description='sii')
        self.assertEqual(category.title, 'first')
        self.assertEqual(category.description, 'sii')

    def test_create_category_count(self):
        Category.objects.create(title='text')
        product_count = Category.objects.count()
        self.assertEqual(product_count, 1)


class TestProductModel(TestCase):

    def test_create_article(self):
        category = Category.objects.create(title='first', description='sii')
        gender = Gender.objects.create(gender='male')
        user = CustomUser.objects.create(email='lalafo@gmail.com', first_name='Murat',
                                         last_name='Darmianov', description='kkk',
                                         sent_at=datetime.now, gender=gender, city='Bishkek')
        product = Products.objects.create(title='first', description='sii', price=500,
                                           created_at=datetime.now, is_status=True, categ=category,
                                          user=user)
        self.assertEqual(product.title, 'first')
        self.assertEqual(product.description, 'sii')
        self.assertEqual(product.price, 500)
        self.assertEqual(product.created_at, datetime.now)
        self.assertEqual(product.is_status, True)
        self.assertEqual(product.categ, category)
        self.assertEqual(product.user, user)
