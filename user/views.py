from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from names.models import Name
from user.serializers import NameBasedModelSerialiser, NameModelSerialiser


# Create your views here.


class NameListAPIView(ListAPIView):
    queryset = Name.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return NameBasedModelSerialiser
        return NameModelSerialiser
