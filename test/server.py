import unittest

from pyramid import testing
from mockito_demo.server import hello_world


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        # Create Request
        request = testing.DummyRequest()

        # Add name to request
        request.matchdict = {'name': 'bob'}

        # Get and validate response
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)
