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

# from doers.filters import What_is_famousFilter
from doers.models import Success
from doers.serializers import SuccessModelSerializer


# # #PAGINATOR
class SuccessLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


# # # #
class SuccessLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = Success.objects.all()
    serializer_class = SuccessModelSerializer
    pagination_class = SuccessLimitOffsetPagination
