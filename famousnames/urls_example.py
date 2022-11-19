from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from famousnames.view_example import SuccessLimitOffsetPaginationViewSet

router = DefaultRouter()




router.register('success_p',SuccessLimitOffsetPaginationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    #
    path('api/', include(router.urls)),

]
