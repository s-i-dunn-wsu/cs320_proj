# Samuel Dunn
# CS 320, Fall 2019

import os
import cherrypy
from jinja2 import Environment, FileSystemLoader

try:
    from ..tutorial.tutorial_factory import TutorialFactory
    from .tutorial_manager import TutorialManager
    from ..auth.authenticator import Authenticator
except ImportError:
    from pofis.tutorial.tutorial_factory import TutorialFactory
    from pofis.site.tutorial_manager import TutorialManager
    from pofis.auth.authenticator import Authenticator

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
    
    @cherrypy.expose
    def create_user(self, user_name = None, password = None, conf_password = None):
        """
        """
        # starting page
        if not user_name and not password and not conf_password:
            template = self.env.get_template('create_user.html')
            return template.render()
        else: # check user input
            template = self.env.get_template('create_user.html')

            if user_name is None and password is None and conf_password is None:
                return template.render()            
            
            # check if passwords entered match
            if password == conf_password:
                # password not correct format
                if len(password) < 6 or len(password) > 10 and any(password.isdigit()):
                    return template.render(username = user_name, success = False, reason = "Password must be between 6 to 10 digits and include 1 number")
                elif user_name is None: 
                    return template.render(success = False, reason = "No username entered")
                elif not Authenticator().check_for_user_exist(user_name):
                    return template.render(username = user_name, success = True, reason = "")
                else:
                    # the username is taken.
                    return template.render(username = user_name, success = False, reason = "Username is taken")
            else:
                return template.render(username = user_name, success = False, reason = "Passwords do not match")
        
        # if everything works out
        Authenticator().create_user(user_name, password)
        raise cherrypy.HTTPRedirect('/')