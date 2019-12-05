# Samuel Dunn
# CS 320, Fall 2019

import unittest
import os
import sys
from pofis.r_eval.uce import UserCodeEvaluator

# this helps a test case do the right thing:
ground_truth_builtins = {k: v for k, v in __builtins__.items()}
stdout = sys.stdout
stderr = sys.stderr

class UCETests(unittest.TestCase):

    def test_construction(self):
        """
        Tests to ensure that UserCodeEvaluator can construct
        """
        UserCodeEvaluator()

    def test_runs_script(self):
        """
        Tests that UCE evaluates and returns the expected module data
        """
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, 'example_script.txt')) as fd:
            user_code = fd.read()

        uce = UserCodeEvaluator()
        module, output, error = uce.eval(user_code)

        self.assertEqual('foo was called\n', output)

        for attr in ('x', 'y', 'z', 'foo'):
            self.assertIn(attr, module)

        self.assertEqual(module['z'], 47)

        with self.assertRaises(ValueError):
            module['throws_exception_on_x_eq_13'](13)

    def test_restores_state(self):
        """
        Tests to ensure that everything that is tweaked when executing
        user code is returned to its proper state.
        """
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, 'example_script.txt')) as fd:
            user_code = fd.read()

        uce = UserCodeEvaluator()
        module, output, error = uce.eval(user_code)

        # now check sys.stderr, sys.stdout and all items in __builtins__
        self.assertEqual(sys.stdout, stdout, "stdout is restored")
        self.assertEqual(sys.stderr, stderr, "stderr is restored")

        for k, v in ground_truth_builtins.items():
            self.assertEqual(__builtins__[k], v, f"{repr(k)} in __builtins__ is preserved")


if __name__ == "__main__":
    unittest.main()