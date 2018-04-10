from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world_get(request):
    return Response('Hello World!')


def hello_world_post(request):
    return Response('Hello %(name)s!' % request.matchdict)


if __name__ == '__main__':
    with Configurator() as config:
        # Dumb Hello World
        config.add_route('hello', '/hello/{name}')
        config.add_view(hello_world_post, route_name='hello', request_method="POST")
        config.add_view(hello_world_get, route_name='hello', request_method="GET")

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
