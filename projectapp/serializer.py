from rest_framework.serializers import ModelSerializer
from .models import Project
from .models import ToDo


class ProjectSerializer(ModelSerializer):
    # настройка сериалайзера,Foreign Key, ManytoMany
    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ('is_active',)
