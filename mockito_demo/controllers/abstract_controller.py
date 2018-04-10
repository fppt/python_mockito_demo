from abc import ABCMeta


class AbstractController(object):
    __metaclass__ = ABCMeta

    def __init__(self, request):
        self.request = request
