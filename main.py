from flask import Flask, request, render_template
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)


class Website(graphene.ObjectType):
    url = graphene.String(required=True)
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()


class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f"Hello {name}!"

    def resolve_goodbye(root, info):
        return "See ya!"


schema = Schema(query=Query)


@app.route("/")
def index():
    return render_template("index.html")


app.add_url_rule("graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))


if __name__ == "__main__":
    app.run(debug=True)
