
import os
import json
from ..auth import Authenticator
from .tsf import TestSuiteFactory

class ProgressTracker(object):
    def __init__(self, username):
        self._username = username
        self._user_dir = Authenticator().get_user_data_dir(username)
        self._user_prog_file = os.path.join(self._user_dir, 'completed_suites.json')
        if not os.path.exists(self._user_prog_file):
            with open(self._user_prog_file, 'w') as fd:
                json.dump({}, fd)

    def load_user_progress(self):
        """
        """
        with open(self._user_prog_file) as fd:
            completed_suites = json.load(fd)

        for suite_id in TestSuiteFactory().suite_ids():
            yield (suite_id,
                TestSuiteFactory().get_suite_name(suite_id),
                str(suite_id) in completed_suites,
                TestSuiteFactory().get_suite_refdoc(suite_id))

    def mark_passed(self, suite_num: int):
        """
        """
        with open(self._user_prog_file) as fd:
            completed_suites = json.load(fd)

        completed_suites[str(suite_num)] = None

        with open(self._user_prog_file, 'w') as fd:
            json.dump(completed_suites, fd)

    def has_progress(self, suite_id):
        """
        Returns a boolean to indicate if the user has progress on this particular suite.
        """
        return f"{suite_id}.txt" in os.listdir(self._user_dir)


    def save_progress(self, suite_id, user_code):
        """
        Saves the users current progress so it can be restored later.
        """
        with open(os.path.join(self._user_dir, f'{suite_id}.txt'), 'w') as fd:
            fd.write(user_code)

    def delete_progress(self, suite_id):
        try:
            os.remove(os.path.join(self._user_dir, f'{suite_id}.txt'))
        except OSError:
            print(f"Attempted to delete suite {suite_id} for user {self._username} but failed!")

    def update(self, test_suite):
        """
        """
        with open(os.path.join(self._user_dir, f'{test_suite._id}.txt')) as fd:
            test_suite._body = fd.read()