from rest_framework.viewsets import ModelViewSet

from .models import Project, ToDo
from .serializer import ProjectSerializer, ToDoSerializer


# Create your views here.
class ProjectViewSet:
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
