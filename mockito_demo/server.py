from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

from mockito_demo.controllers.manager_controller import ManagerController
from mockito_demo.manager.manager import Manager


@view_config(route_name='hello-get', request_method='GET')
def hello_world_get(request):
    return Response('Hello World!')

@view_config(route_name='hello-post', request_method='POST')
def hello_world_post(request):
    return Response('Hello %(name)s!' % request.matchdict)


if __name__ == '__main__':
    #manager_controller = ManagerController(Manager())

    with Configurator() as config:
        # Dumb Hello World
        config.add_route('hello-get', '/hello')
        config.add_route('hello-post', '/hello/{name}')

        # Manager GET
        config.add_route('manager-get', '/manager')
        # Manager POST
        config.add_route('manager-post', '/manager/{job_type}')

        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
