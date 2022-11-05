from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Name, Biography, What_is_famous


class NameModelSerializer(ModelSerializer):
    class Meta:
        model = Name
        fields = ('first_name', 'last_name', 'birthday_year', 'place_of_birth')
            # ('first_name', 'last_name', 'birthday_year', 'place_of_birth')
        # fields = ('first_name', 'last_name') выводит нужные колич полей
        # exclude = ('first_name' ) нужное поле исключить ,остальные выведи


class NameBasedModelSerialiser(ModelSerializer):
    class Meta:
        model = Name
        fields = ('first_name', 'birthday_year')


class BiographyModelSerializer(HyperlinkedModelSerializer):
    # name = NameModelSerializer()
    class Meta:
        model = Biography
        fields = '__all__'


class What_is_famousModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = What_is_famous
        fields = '__all__'
