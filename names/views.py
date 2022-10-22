from rest_framework.viewsets import ModelViewSet
from .models import Name
from .serializers import NameModelSerializer


# Create your views here.

class NameModelViewSet(ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameModelSerializer
