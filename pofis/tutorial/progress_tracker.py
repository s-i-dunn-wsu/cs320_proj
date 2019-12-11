
import os
import json
from ..auth import Authenticator
from .tutorial_factory import TutorialFactory

class ProgressTracker(object):
    def __init__(self, username):
        self._username = username
        self._user_dir = Authenticator().get_user_data_dir(username)
        self._user_prog_file = os.path.join(self._user_dir, 'completed_tutorials.json')
        if not os.path.exists(self._user_prog_file):
            with open(self._user_prog_file, 'w') as fd:
                json.dump({}, fd)

    def load_user_progress(self):
        """
        """
        with open(self._user_prog_file) as fd:
            completed_tutorials = json.load(fd)

        for tutorial_id in TutorialFactory().tutorial_ids():
            yield (tutorial_id,
                TutorialFactory().get_tutorial_name(tutorial_id),
                str(tutorial_id) in completed_tutorials,
                TutorialFactory().get_tutorial_refdoc(tutorial_id))

    def mark_passed(self, tutorial_num: int):
        """
        """
        with open(self._user_prog_file) as fd:
            completed_tutorials = json.load(fd)

        completed_tutorials[str(tutorial_num)] = None

        with open(self._user_prog_file, 'w') as fd:
            json.dump(completed_tutorials, fd)

    def has_progress(self, tutorial_id):
        """
        Returns a boolean to indicate if the user has progress on this particular tutorial.
        """
        return f"{tutorial_id}.txt" in os.listdir(self._user_dir)

    def save_progress(self, tutorial_id, user_code):
        """
        Saves the users current progress so it can be restored later.
        """
        with open(os.path.join(self._user_dir, f'{tutorial_id}.txt'), 'w') as fd:
            fd.write(user_code)

    def delete_progress(self, tutorial_id):
        try:
            os.remove(os.path.join(self._user_dir, f'{tutorial_id}.txt'))
        except OSError:
            print(f"Attempted to delete tutorial {tutorial_id} for user {self._username} but failed!")

    def update(self, test_tutorial):
        """
        """
        with open(os.path.join(self._user_dir, f'{test_tutorial._id}.txt')) as fd:
            test_tutorial._body = fd.read()