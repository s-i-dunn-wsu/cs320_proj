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
        self._prompt = "#this is some example python code.\nimport random\nfoo=lambda n: random.randint(1, n)\n"

    def evaluate_runtime(self, module):
        """
        Evaluates the contents of the given module (executed via runpy, probably)
        against thist TestSuite's configured criteria.
        """

    @property
    def prompt(self):
        return self._prompt
