
import cherrypy

from ..tutorial.progress_tracker import ProgressTracker
from ..tutorial.tutorial_factory import TutorialFactory

@cherrypy.expose
class TutorialManager(object):
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

        template = self.env.get_template('tutorial_overview.html')
        return template.render(username=cherrypy.request.login, tutorial_data=user_progress.load_user_progress())

    @cherrypy.expose
    def take_tutorial(self, tutorial_num=0):
        """
        Loads the tutorial object and directs the user to an editing session.
        """
        tutorial = TutorialFactory().get_tutorial(tutorial_num)

        user_progress = ProgressTracker(cherrypy.request.login)
        if user_progress.has_progress(tutorial_num):
            user_progress.update(tutorial)

        template = self.env.get_template('tutorial.html')
        return template.render(tutorial = tutorial, tutorial_id = tutorial_num)

    @cherrypy.expose
    def save(self, tutorial_id, user_code):
        """
        Saves the contents of user_code to the user's folder.
        """
        user_progress = ProgressTracker(cherrypy.request.login)
        user_progress.save_progress(tutorial_id, user_code)

    @cherrypy.expose
    def delete(self, tutorial_id):
        """
        """
        user_progress = ProgressTracker(cherrypy.request.login)
        user_progress.delete_progress(tutorial_id)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def evaluate(self, tutorial_id, user_code):
        """
        Evaluates the usercode and responds with teh pass/fail data as JSON.
        """
        # Evaluate the user code (hopefully in a recoverable way)

        # Prepare response
        eval_result = True
        eval_reason = "Testing failure handling"

        # Note: should ensure user progress is updated according to eval_result


        # Reply with repsonse.
        return {'pass': eval_result, "reason": eval_reason}
