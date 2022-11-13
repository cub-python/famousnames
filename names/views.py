from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from user.serializers import NameModelSerialiser
from .models import Name, Biography, What_is_famous
from .serializers import BiographyModelSerializer, What_is_famousModelSerializer, \
    NameBasedModelSerialiser


# Create your views here.
# class NameModelViewSet(mixins.ListModelMixin,
#                        mixins.RetrieveModelMixin,
#                        mixins.UpdateModelMixin,
#                        viewsets.GenericViewSet):
#     queryset = Name.objects.all()
#     serializer_class = NameModelSerializer


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.name.is_staff


class NameModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Name.objects.all()

    # serializer_class = NameModelSerializer
    # permission_classes = [IsAdminUser]
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return NameBasedModelSerialiser
        return NameModelSerialiser


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class What_is_famousModelViewSet(ModelViewSet):
    queryset = What_is_famous.objects.all()
    serializer_class = What_is_famousModelSerializer
