from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Project, ToDo
from .serializer import ProjectSerializer, ToDoSerializer


# Create your views here.
class ProjectPagination(PageNumberPagination):
    page_size = 10


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectPagination

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset


class ToDoViewSet(PageNumberPagination):
    page_size = 10
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
