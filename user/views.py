#
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import ListAPIView
#
from user.serializers import DoerBaseModelSerialiser, DoerModelSerialiser
# #
# #
# # # Create your views here.
# #
# #
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return DoerBaseModelSerialiser
        return DoerModelSerialiser
