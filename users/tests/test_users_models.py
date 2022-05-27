from datetime import datetime

from django.test import TestCase

from users.models import CustomUser, Gender


class TestProductModel(TestCase):

    def test_create_users(self):
        gender = Gender.objects.create(gender='male')
        user = CustomUser.objects.create(email='lalafo@gmail.com', first_name='Murat',
                                         last_name='Darmianov', description='kkk',
                                         sent_at=datetime.now, gender=gender, city='Bishkek')
        self.assertEqual(user.email, 'lalafo@gmail.com')
        self.assertEqual(user.first_name, 'Murat')
        self.assertEqual(user.last_name, 'Darmianov')
        self.assertEqual(user.description, 'kkk')
        self.assertEqual(user.sent_at, datetime.now)
        self.assertEqual(user.gender, gender)
        self.assertEqual(user.city, 'Bishkek')
