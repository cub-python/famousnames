from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Biography, Doer, Success


class DoerModelSerialiser(ModelSerializer):
    class Meta:
        model = Doer
        fields = '__all__'
        # fields = ('first_name', 'last_name', 'birthday_year', 'place_of_birth')
        # ('first_name', 'last_name', 'birthday_year', 'place_of_birth')
        # fields = ('first_name', 'last_name') выводит нужные колич полей
        # exclude = ('first_name' ) нужное поле исключить ,остальные выведи


class DoerBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Doer
        fields = ('first_name', 'birthday_year')


class BiographyModelSerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class SuccessModelSerializer(ModelSerializer):
    class Meta:
        model = Success
        fields = '__all__'


