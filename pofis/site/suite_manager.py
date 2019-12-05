
import cherrypy

from ..test_suite.progress_tracker import ProgressTracker
from ..test_suite.tsf import TestSuiteFactory

@cherrypy.expose
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

        user_progress = ProgressTracker(cherrypy.request.login)
        if user_progress.has_progress(suite_num):
            user_progress.update(test_suite)

        template = self.env.get_template('suite.html')
        return template.render(testsuite = test_suite, test_id = suite_num)

    @cherrypy.expose
    def save(self, suite_id, user_code):
        print(f"{cherrypy.request.login} saved their progress for suite: {suite_id}")
        user_progress = ProgressTracker(cherrypy.request.login)
        user_progress.save_progress(suite_id, user_code)

    @cherrypy.expose
    def delete(self, suite_id):
        """
        """
        user_progress = ProgressTracker(cherrypy.request.login)
        user_progress.delete_progress(suite_id)