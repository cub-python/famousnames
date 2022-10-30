from rest_framework import mixins, viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Name, Biography, What_is_famous
from .serializers import NameModelSerializer, BiographyModelSerializer, What_is_famousModelSerializer


# Create your views here.
# class NameModelViewSet(mixins.ListModelMixin,
#                        mixins.RetrieveModelMixin,
#                        mixins.UpdateModelMixin,
#                        viewsets.GenericViewSet):
#     queryset = Name.objects.all()
#     serializer_class = NameModelSerializer

class NameModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Name.objects.all()
    serializer_class = NameModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class What_is_famousModelViewSet(ModelViewSet):
    queryset = What_is_famous.objects.all()
    serializer_class = What_is_famousModelSerializer
