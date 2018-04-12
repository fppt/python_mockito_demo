from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello-get', request_method='GET')
def hello_world_get(_):
    return Response('Hello World!')


@view_config(route_name='hello-post', request_method='POST')
def hello_world_post(request):
    return Response('Hello %(name)s!' % request.matchdict)


if __name__ == '__main__':
    with Configurator() as config:
        # Dumb Hello World
        config.add_route('hello-get', '/hello')
        config.add_route('hello-post', '/hello/{name}')

        # Worker
        config.add_route('worker', '/worker/{job_type}')

        config.scan()
        config.scan('controllers')
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
