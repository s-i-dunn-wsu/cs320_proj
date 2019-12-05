# Samuel Dunn
# CS 320, Fall 2019

import os
import cherrypy
from jinja2 import Environment, FileSystemLoader

try:
    from ..test_suite.tsf import TestSuiteFactory
except ImportError:
    from pofis.test_suite.tsf import TestSuiteFactory

class Root(object):
    def __init__(self):
        here = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(here, 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))

    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect('/refdocs/index.html')

    @cherrypy.expose
    def login(self):
        return "Placeholder"

    @cherrypy.expose
    def suites(self, **params):
        """
        Loads the suite progress for the logged in user.
        """

        if not cherrypy.request.login:
            raise cherrypy.HTTPError(401)

        return "You made it!"

    @cherrypy.expose
    def suite(self, id=0, user_auth=None):
        """
        """
        if not isinstance(id, int):
            id = int(id)

        # Get the associated TestSuite object.
        ts = TestSuiteFactory().get_suite(id)

        # Now get the template
        template = self.env.get_template('suite.html')

        return template.render(testsuite = ts)
