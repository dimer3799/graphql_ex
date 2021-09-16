import graphene
import extraction
import requests


def extract(url):
    html = requests.get(url).text
    extracted = extraction.Extractor().extract(html, source_url=url)
    print(extracted)
    return extracted


class WRent(graphene.ObjectType):
    """url = graphene.String(required=True)
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()"""

    name = graphene.String()


class Query(graphene.ObjectType):
    website = graphene.Field(test=graphene.List(graphene.String))

    def resolve_website(self, info, url):
        extracted = extract(url)
        return ["Website()" for i in range(9)]


schema = graphene.Schema(query=Query)
