# Samuel Dunn
# CS 320, Fall 2019
# Telos Security Force.py
# Jk, TestSuiteFactory.

import os
import json
from ._ts import TestSuite

class TestSuiteFactory(object):
    # see this: https://subscription.packtpub.com/book/application_development/9781783283378/2/ch02lvl1sec16/the-borg-singleton
    # I do it a little differently (no need to override __new__, generally this will reduce execution over overloading __new__
    # by approx 0.02 seconds per 100,000 accesses)
    __borg_state = None
    def __init__(self):
        """
        """
        if TestSuiteFactory.__borg_state == None:
            TestSuiteFactory.__borg_state = self.__dict__
            self._here = here = os.path.dirname(os.path.abspath(__file__))

            # Load test suite info.
            with open(os.path.join(self._here, 'suite_data.json')) as fd:
                self._suite_data = json.load(fd)

        else:
            self.__dict__ = TestSuiteFactory.__borg_state

    def suite_ids(self):
        for key in self._suite_data:
            yield key

    def get_suite_name(self, suite_id) -> str:
        """
        Returns a user-legible suite name.
        """
        if str(suite_id) in self._suite_data:
            return self._suite_data[str(suite_id)]['name']

    def get_suite_refdoc(self, suite_id) -> str:
        """
        Returns the href to the reference document most closely associated with this 
        test suite (tutorial)
        """
        if suite_id in self._suite_data:
            print(f"Have suite: {suite_id}")
            if 'Refdoc_Href' in self._suite_data[suite_id]:
                href = self._suite_data[suite_id]['Refdoc_Href']
                print(f"suite {suite_id} has 'Refdoc_Href': as {href}")
                return href

    def get_suite(self, suite_id) -> TestSuite:
        """
        """
        if suite_id not in self._suite_data:
            return None

        ts = TestSuite()
        ts._id = suite_id

        # load the prompt string, stick to english locale for now.
        with open(os.path.join(self._here, 'prompt_strings', 'en', f'{suite_id}.txt')) as fd:
            ts._body = fd.read()

        # Now load and assign the test suite name and criteria.
        with open(os.path.join(self._here, 'suite_data.json')) as fd:
            ts._name = self._suite_data[suite_id]['name']
            ts._criteria = self._suite_data[suite_id]['criteria']

            if 'prog_lang' in self._suite_data[suite_id]:
                ts._lang = self._suite_data[suite_id]['prog_lang']

            if 'help_text' in self._suite_data[suite_id]:
                ts._help_text = self._suite_data[suite_id]['help_text']

        return ts