from django.contrib import admin
from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .schema import schema
#https://github.com/graphql-python/graphene-django/issues/61
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('director/',views.show_directors, name='show_directors'),
    path('movie/',views.show_movies, name='show_movies'),
    path('add_director/',views.add_director, name='add_director'),
    path('add_movie/',views.add_movie, name='add_movie'),
    path('movie/<int:movie_id>/edit_director/',views.edit_director,name='edit_director'),
    path('graphql/',csrf_exempt(GraphQLView.as_view(
        graphiql=True,
        schema=schema
    ))),
]
