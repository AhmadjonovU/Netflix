from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from rest_framework.generics import CreateAPIView
from netflixapp.views import MovieList
from netflixapp.views import DelateActor
from netflixapp.serializer import CommentSerializer
from netflixapp.views import CreateActor,anActor,ActorList,CommentViewSet,ActorViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

doc_view = get_schema_view(
    openapi.Info(
        title = "Netflix",
        default_version = "v1",
        description="( REST API) Clone of Netflix using Django Rest Framework",
        contact = openapi.Contact("Umidjon Ahmadjonov <ahmadjonovumidjon782@gmail.com>"),

    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register('actor',ActorViewSet)
router.register('comment',CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path("aktor/", ActorList.as_view()),
    path("actor/<int:pk>", anActor.as_view()),
    path('actors/', CreateActor.as_view()),
    path('udalit/<int:pk>',DelateActor.as_view()),
    path('doc/',doc_view.with_ui("swagger", cache_timeout=0), name="swagger_doc"),
    path('redoc/',doc_view.with_ui("redoc", cache_timeout=0), name="redoc_doc"),
    path('movie/',MovieList.as_view())
]
