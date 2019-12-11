# Samuel Dunn
# CS 320, Fall 2019

import os
import cherrypy
from jinja2 import Environment, FileSystemLoader

try:
    from ..tutorial.tutorial_factory import TutorialFactory
    from .tutorial_manager import TutorialManager
except ImportError:
    from pofis.tutorial.tutorial_factory import TutorialFactory
    from pofis.site.tutorial_manager import TutorialManager

class Root(object):
    def __init__(self):
        here = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(here, 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))

        self.tutorials = TutorialManager(self.env)
        self.tutorials.expose = True

    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect('/refdocs/index.html')

    @cherrypy.expose
    def login(self):
        # The user successfully logged in (otherwise they'd have gotten a 401)
        # Lets just return them to where they were
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def suite(self, id=0):
        """
        """
        if not isinstance(id, int):
            id = int(id)

        # Get the associated Tutorial object.
        t = TutorialFactory().get_suite(id)

        # Now get the template
        template = self.env.get_template('suite.html')

        return template.render(tutorial = t)

