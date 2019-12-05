# Samuel Dunn
# CS 320, Fall 2019

import os
import cherrypy
from jinja2 import Environment, FileSystemLoader

try:
    from ..test_suite.tsf import TestSuiteFactory
    from .suite_manager import SuiteManager
except ImportError:
    from pofis.test_suite.tsf import TestSuiteFactory
    from pofis.site.suite_manager import SuiteManager

class Root(object):
    def __init__(self):
        here = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(here, 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))

        self.suites = SuiteManager(self.env)
        self.suites.expose = True

    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect('/refdocs/index.html')

    @cherrypy.expose
    def login(self):
        # The user successfully logged in (otherwise they'd have gotten a 401)
        # Lets just return them to where they were
        raise cherrypy.HTTPRedirect('/')

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

