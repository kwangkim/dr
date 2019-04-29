# Ref https://www.youtube.com/watch?v=-0uxxht4mko
import graphene
from graphene_django.types import DjangoObjectType
from .models import Director, Movie
class DirectorType(DjangoObjectType):
    class Meta:
        model = Director

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
class Query(graphene.ObjectType):
    directors=graphene.List(DirectorType)
    movies=graphene.List(MovieType)

    def resolve_directors(self,context):
        return Director.objects.all()

    def resolve_movies(self,context):
        return Movie.objects.all()

schema = graphene.Schema(query=Query)