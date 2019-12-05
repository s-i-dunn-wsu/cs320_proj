# Samuel Dunn
# CS 320, Fall 2019
# This file provides the TestSuite class.

class TestSuite(object):
    """
    TestSuite encapsulates all the data associated to, well, test suites given to users.
    It supplies properties and methods necessary for populating tests with pre-text and,
    inspecting the user's evlauated code for correctness, and supplying strings for when
    a test fails.
    """
    def __init__(self):
        """
        NOTE: do not use directly, use TestSuiteFactory instead.
        """
        self._body = ""
        self._help_text = ""
        self._lang = 'python'
        self._criteria = [],
        self._id = 0

    def evaluate_runtime(self, module, out, err):
        """
        Evaluates the contents of the given module (executed via runpy, probably)
        against thist TestSuite's configured criteria.

        :returns: tuple, the first entry is pass/fail, the second is the cause of failure should the eval fail.
        """
        for eval_string in self._criteria:
            if not eval(eval_string):
                return False, eval_string

        return True, None

    @property
    def body(self):
        return self._body

    @property
    def help_text(self):
        return self._help_text

    @property
    def lang(self):
        """
        Determines which language mode to put the ACE editor in
        """
        return self._lang