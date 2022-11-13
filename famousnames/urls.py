"""famousnames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from graphene_django.views import GraphQLView

from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from names.views import NameModelViewSet, What_is_famousModelViewSet, BiographyModelViewSet
from projectapp.views import ProjectViewSet, ToDoViewSet
from user.views import NameListAPIView

# from projectapp.views import ProjectViewSet, ToDoViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='famousnames',
        default_version='v2',
        description='Project',
        contact=openapi.Contact(email='test@mail.ru'),
        license=openapi.License(name='ST License')
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,)
)

router = DefaultRouter()
router.register('names', NameModelViewSet)
router.register('What_is_famous', What_is_famousModelViewSet)
router.register('Biography', BiographyModelViewSet)

router.register('projects', ProjectViewSet)
# router.register('todos', ToDoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_auth/', include('rest_framework.urls')),
    path('api/', include(router.urls, )),
    path('api-token-auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger/', schema_view.with_ui('swagger')),
    # path('swagger<str:format>', schema_view.without_ui()),
    path('redoc/', schema_view.with_ui('redoc')),

    # path('api/<str:version>/name/', NameListAPIView.as_view()),
    # path('api/user/v1/', include('user.urls',namespace='v1')),
    # path('api/user/v2/', include('user.urls', namespace='v2')),

    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', TemplateView.as_view(template_name='index.html')),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),

]
