from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from .models import Biography, Success, Doer
from .serializers import BiographyModelSerializer, \
   SuccessModelSerializer, DoerBaseModelSerializer, DoerModelSerialiser


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


class DoerModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Doer.objects.all()

    # serializer_class = NameModelSerializer
    # permission_classes = [IsAdminUser]
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return DoerBaseModelSerializer
        return DoerModelSerialiser


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class SuccessModelViewSet(ModelViewSet):
    queryset = Success.objects.all()
    serializer_class = SuccessModelSerializer
