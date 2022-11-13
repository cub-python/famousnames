from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
# from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
# from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
#     get_object_or_404

# from names.filters import What_is_famousFilter
from names.models import What_is_famous
from names.serializers import What_is_famousModelSerializer


# # #PAGINATOR
class What_is_famousLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


# # # #
class What_is_famousLimitOffsetPaginatonViewSet(ModelViewSet):
    queryset = What_is_famous.objects.all()
    serializer_class = What_is_famousModelSerializer
    pagination_class = What_is_famousLimitOffsetPagination
