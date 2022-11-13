from django.urls import path

from user.views import NameListAPIView

app_name = 'name'

urlpatterns = [
    path('', NameListAPIView.as_view),
]
