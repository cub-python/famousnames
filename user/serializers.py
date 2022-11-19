
from rest_framework.serializers import ModelSerializer

from doers.models import Doer



class DoerModelSerialiser(ModelSerializer):
    class Meta:
        model = Doer
        fields = ('first_name','last_name', 'place_of_birth')
        # fields = ('first_name', 'last_name') выводит нужные колич полей
        # exclude = ('first_name' ) нужное поле исключить ,остальные выведи


class DoerBaseModelSerialiser(ModelSerializer):
    # name = NameModelSerializer()
    class Meta:
        model = Doer
        fields = ('first_name', 'last_name', 'birthday_year')



