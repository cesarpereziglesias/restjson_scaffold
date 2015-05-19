# -*- coding: utf-8 -*-
from pyramid.view import view_defaults

@view_defaults(renderer='json')
class View(object):

    def __init__(self, request):
        self._request = request
