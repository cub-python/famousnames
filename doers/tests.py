import math

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIClient, APISimpleTestCase, APIRequestFactory
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .models import Doer, Biography
from .views import DoerModelViewSet


# Create your tests here.

class TestDoerViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin123'
        self.data = {'first_name': 'Иосиф', 'last_name': 'Сталин', 'birthday_year': 1878}
        self.data_put = {'first_name': 'Карл', 'last_name': 'Маркс', 'birthday_year': 1818}
        self.url = '/api/doers/'
        self.admin = User.objects.create_superuser(self.name, self.password)

    # APIRequestFactory,force_authenticate
    def test_get_list(self):
        #
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = DoerModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_quest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        view = DoerModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        force_authenticate(request, self.admin)
        view = DoerModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # APIClient
    def test_get_detail(self):
        client = APIClient()
        doer = Doer.objects.create(**self.data)
        response = client.get(f'{self.url}{doer.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_guest(self):
        client = APIClient()
        doer = Doer.objects.create(**self.data)
        response = client.put(f'{self.url}{doer.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_admin(self):
        client = APIClient()
        doer = Doer.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url}{doer.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        doer = Doer.objects.get(id=doer.id)
        self.assertEqual(doer.first_name, self.data_put.get('first_name'))
        self.assertEqual(doer.last_name, self.data_put.get('last_name'))
        self.assertEqual(doer.birthday_year, self.data_put.get('birthday_year'))

        client.logout()

    # APISimpleTestCase
    class TestMath(APISimpleTestCase):

        def test_sqrt(self):
            self.assertEqual(math.sqrt(4), 2)

    # APITestCase
    class TestBiography(APITestCase):

        def setUp(self) -> None:
            self.name = 'admin'
            self.password = 'admin123'

            self.data = {'first_name': 'Иосиф', 'last_name': 'Сталин', 'birthday_year': 1878}
            self.data_put = {'first_name': 'Карл', 'last_name': 'Маркс', 'birthday_year': 1818}
            self.url = '/api/biography/'
            self.admin = User.objects.create_superuser(self.name, self.password)

        def test_get_list(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_put_admin(self):
            doer = Doer.objects.create(**self.data)
            bio = Biography.objects.create(text='test', doer=doer)
            self.client.login(username=self.name, password=self.password)
            response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'name': bio.name.id})
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            bio_ = Biography.objects.get(id=bio.id)
            self.assertEqual(bio_.text, 'Biography')
            self.client.logout()

        def test_put_mixer(self):
            bio = mixer.blend(Biography)
            self.client.login(username=self.name, password=self.password)
            response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'name': bio.name.id})
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            bio_ = Biography.objects.get(id=bio.id)
            self.assertEqual(bio_.text, 'Biography')
            self.client.logout()

        def test_put_mixer_fields(self):
            bio = mixer.blend(Biography, text='Биография')
            self.assertEqual(bio.text, 'Биография')
            self.client.login(username=self.name, password=self.password)
            response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'name': bio.name.id})
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            bio_ = Biography.objects.get(id=bio.id)
            self.assertEqual(bio_.text, 'Biography')
            self.client.logout()
