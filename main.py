from flask import Flask, request, render_template
from graphene import ObjectType, String, Schema


app = Flask(__name__)


class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    schema = Schema(query=Query)
    return render_template('api.html')


if __name__ == '__main__':
    app.run(debug=True)


schema = Schema(query=Query)
