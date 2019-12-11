# Samuel Dunn
# CS 320, Fall 2019
# Telos Security Force.py
# Jk, TutorialFactory.

import os
import json
from ._tutorial import Tutorial

class TutorialFactory(object):
    # see this: https://subscription.packtpub.com/book/application_development/9781783283378/2/ch02lvl1sec16/the-borg-singleton
    # I do it a little differently (no need to override __new__, generally this will reduce execution over overloading __new__
    # by approx 0.02 seconds per 100,000 accesses)
    __borg_state = None
    def __init__(self):
        """
        """
        if TutorialFactory.__borg_state == None:
            TutorialFactory.__borg_state = self.__dict__
            self._here = here = os.path.dirname(os.path.abspath(__file__))

            # Load tutorial info.
            with open(os.path.join(self._here, 'tutorial_data.json')) as fd:
                self._tutorial_data = json.load(fd)

        else:
            self.__dict__ = TutorialFactory.__borg_state

    def tutorial_ids(self):
        for key in self._tutorial_data:
            yield key

    def get_tutorial_name(self, tutorial_id) -> str:
        """
        Returns a user-legible tutorial name.
        """
        if str(tutorial_id) in self._tutorial_data:
            return self._tutorial_data[str(tutorial_id)]['name']

    def get_tutorial_refdoc(self, tutorial_id) -> str:
        """
        Returns the href to the reference document most closely associated with this
        tutorial
        """
        if tutorial_id in self._tutorial_data:
            if 'Refdoc_Href' in self._tutorial_data[tutorial_id]:
                href = self._tutorial_data[tutorial_id]['Refdoc_Href']
                return href

    def get_tutorial(self, tutorial_id) -> Tutorial:
        """
        Constructs and returns the appropriate Tutorial object.
        """
        if tutorial_id not in self._tutorial_data:
            return None

        t = Tutorial()
        t._id = tutorial_id

        # load the prompt string, stick to english locale for now.
        with open(os.path.join(self._here, 'prompt_strings', 'en', f'{tutorial_id}.txt')) as fd:
            t._body = fd.read()

        # Now load and assign the tutorial name and criteria.
        t._name = self._tutorial_data[tutorial_id]['name']
        t._criteria = self._tutorial_data[tutorial_id]['criteria']

        if 'prog_lang' in self._tutorial_data[tutorial_id]:
            t._lang = self._tutorial_data[tutorial_id]['prog_lang']

        if 'help_text' in self._tutorial_data[tutorial_id]:
            t._help_text = self._tutorial_data[tutorial_id]['help_text']

        return t