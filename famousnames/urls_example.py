from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()


class What_is_famousLimitOffsetPaginatonViewSet:
    pass


router.register('What_is_famous_p', What_is_famousLimitOffsetPaginatonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    #
    path('api/', include(router.urls)),

]
