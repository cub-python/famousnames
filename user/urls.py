from django.urls import path

from user.views import NameListAPIView

app_name = 'user'

urlpatterns = [
    path('', NameListAPIView.as_view),
]
