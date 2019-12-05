
import os
import json
from ..auth import Authenticator
from .tsf import TestSuiteFactory

class ProgressTracker(object):
    def __init__(self, username):
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
            yield (suite_id, TestSuiteFactory().get_suite_name(suite_id), str(suite_id) in completed_suites)

    def mark_passed(self, suite_num: int):
        """
        """
        with open(self._user_prog_file) as fd:
            completed_suites = json.load(fd)

        completed_suites[str(suite_num)] = None

        with open(self._user_prog_file, 'w') as fd:
            json.dump(completed_suites, fd)
