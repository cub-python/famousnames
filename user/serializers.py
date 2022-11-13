from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from names.models import Name


class NameModelSerialiser(ModelSerializer):
    class Meta:
        model = Name
        fields = ('first_name','last_name', 'place_of_birth')
        # fields = ('first_name', 'last_name') выводит нужные колич полей
        # exclude = ('first_name' ) нужное поле исключить ,остальные выведи


class NameBasedModelSerialiser(ModelSerializer):
    # name = NameModelSerializer()
    class Meta:
        model = Name
        fields = ('first_name', 'last_name', 'birthday_year')
