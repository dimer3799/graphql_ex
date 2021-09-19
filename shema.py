import graphene
import extraction
from graphene import ObjectType, String, Int, List, Float
import requests


class People(ObjectType):

    name = String()
    ege = Int()
    login = String()
    kpy = Float()


class Query:

    search_worker = List(People, name=String(), ege=Int(), login=String(), kpy=Float())


dim = [People(name="Test", ege=i) for i in range(5)]


class Query(graphene.ObjectType):
    hello = graphene.List(People)

    def resolve_hello(self, info):
        return dim
        return [People(name="Dim", ege=31), People(name="Test", ege=19)]


schema = graphene.Schema(query=Query)
