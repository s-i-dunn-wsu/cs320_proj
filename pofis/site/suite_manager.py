
import cherrypy

from ..test_suite.progress_tracker import ProgressTracker
from ..test_suite.tsf import TestSuiteFactory

class SuiteManager(object):
    def __init__(self, env):
        """
        """
        self.env = env

    @cherrypy.expose
    def index(self):
        if not cherrypy.request.login:
            raise cherrypy.HTTPError(401)

        # Load the user's progress and fill out the suite_overview template.
        user_progress = ProgressTracker(cherrypy.request.login)

        template = self.env.get_template('suite_overview.html')
        return template.render(username=cherrypy.request.login, suite_data=user_progress.load_user_progress())

    @cherrypy.expose
    def take_suite(self, suite_num=0):
        """
        Loads the suite object and directs the user to an editing session.
        """
        test_suite = TestSuiteFactory().get_suite(suite_num)

        template = self.env.get_template('suite.html')
        return template.render(testsuite = test_suite)