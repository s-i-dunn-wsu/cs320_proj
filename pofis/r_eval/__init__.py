# Samuel Dunn
# CS 320, Fall 2019
# This files makes the `r_eval` directory a python module.

# The r_eval module is responsible for taking python source code and
# evaluating its contents in an as-safe-as-possible way.
# To accomplish this, it'll set up an enviroment with most, hopefully all,
# means of interacting with the host system mocked out
# and difficult to access from user space.

# To start, we'll mock out `os`, `sys`, `open`, and so on.
# For tests that require using these modules/functions we'll use
# the mock objects to evaluate if they were used correctly

# To combine all necessary functionality (prepping the input script, executing it,
# inspecting its output based on some adjustable criteria) we'll use the
# UserCodeExecutor (available in this namespace)

from .uce import UserCodeExecutor