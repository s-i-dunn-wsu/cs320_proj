# Samuel Dunn
# CS 320, Fall 2019
# Telos Security Force.py
# Jk, TestSuiteFactory.

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
        else:
            self.__dict__ = TestSuiteFactory.__borg_state

    def get_suite(self, suite_id: int) -> TestSuite:
        """
        """
        return TestSuite()