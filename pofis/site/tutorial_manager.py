
import cherrypy
import json
import os
import time
import tempfile

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
        t = TutorialFactory().get_tutorial(tutorial_id)

        eval_result, eval_reason = self._handle_evaluation(t, user_code)

        # if eval_result is True then we should mark this off as passed on user progress.
        if eval_result == True:
            # load user progress obj.
            user_progress = ProgressTracker(cherrypy.request.login)
            user_progress.mark_passed(tutorial_id)

        # Reply with repsonse.
        return {'pass': eval_result, "reason": eval_reason}

    def _handle_evaluation(self, tutorial, user_code):
        """
        Utilizes multiprocessing in order to safely sequester
        the evaluation of user code.
        This should provide multiple benefits:
        - Prevents requests from coming in while the interpreter is janked up.
        - Prevents infinite loops from really causing a real issue.
        """
        import multiprocessing as mp

        # Should probably use a threadpool + job tokens that the client's
        # page will then check asynchrounously for success,
        # but we're at the last day and I'm frankly too lazy to engineer
        # on the last day.
        # So instead, for POC, we're just going to thread it out and wait up
        # to 500ms to join it. If it takes longer than 500ms then we'll assume
        # its looping.

        # check for a join every 25ms. up to 20 times.
        with tempfile.TemporaryDirectory() as tmpdir:
            # kick the process off.
            p = mp.Process(target=self._do_eval, args=(tmpdir, tutorial, user_code))
            p.start()

            for _ in range(20):
                p.join(0.025)
                if not p.is_alive():
                    # join success.
                    # fetch results and return them.
                    with open(os.path.join(tmpdir, 'results.json')) as fd:
                        result, reason = json.load(fd)
                        return result, reason

        # if we got here, then the process is rogue.
        p.terminate()
        return False, "Process timed out."

    def _do_eval(self, tmpdir, tutorial_obj, user_code):
        # import and create a UserCodeExecutor.
        from ..r_eval.uce import UserCodeExecutor

        # Execute user code.
        m, o, e = UserCodeExecutor().exec(user_code)

        # Run results through tutorial's criteria.
        result, reason = tutorial_obj.evaluate_runtime(m, o, e)

        # write results to disk.
        with open(os.path.join(tmpdir, 'results.json'), 'w') as fd:
            json.dump([result, reason], fd)

        # Fin.
