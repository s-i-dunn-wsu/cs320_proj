# Samuel Dunn
# CS 320, Fall 2019
import sys

class UserCodeEvaluator(object):
    """
    UserCodeEvaluators are responsible for, surprise, evaluating user code
    in a restricted - and server safe - way.
    """
    def __init__(self):
        """
        """

    @property
    def blacklist(self):
        """
        Returns a tuple that specifies global-level elements
        that are not permitted in user space code.
        """
        return ('__import__', 'open', 'exec', 'eval', 'input')

    def eval(self, user_code: str):
        """
        :param str user_code: the code the user has entered into the browser-editor.

        :return: the evaluated module (treat it carefully), the contents written to stdout and stderr during the code's execution.
        """
        indent = self._identify_indentation(user_code)

        import os
        import runpy
        import tempfile
        import pickle
        import sys

        # Stash values that get adjusted in user space
        to_restore = {k: __builtins__[k] for k in self.blacklist}
        stdout = sys.stdout
        stderr = sys.stderr

        # make the user's code safe with our template.
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, 'safe_eval.tmpl')) as fd:
            template = fd.read()
        # get a temp dir to put code output files in.
        with tempfile.TemporaryDirectory() as td:
            out_file = os.path.join(td, 'out')
            err_file = os.path.join(td, 'err')
            tweaked_code = template.format(out_file_path=out_file, err_file_path=err_file,
                                            user_code=('\n' + user_code).replace('\n', f'\n{indent}'),
                                            blacklist=repr(self.blacklist), indent=indent)

            code_path = os.path.join(td, 'user_code.py')
            with open(code_path, 'w', encoding='utf-8') as fd:
                fd.write(tweaked_code)

            # Run the code with runpy to evaluate the content
            with _UserSpaceContext():
                module_data = runpy.run_path(code_path)

            # gather output file content:
            with open(out_file) as fd:
                eval_out = fd.read()

            with open(err_file) as fd:
                eval_err = fd.read()

        # Return state and output on stdout.
        return module_data, eval_out, eval_err

    def _identify_indentation(self, user_code):
        """
        Analyzes user's code and identifies which character(s) are used for indentation
        be it \t, or some amount of space characters.
        returns a string of that sequence.
        This is used to mitigate conflict between the safe-evaluation template and user's code.
        """

        # for now, just return 4 spaces (this is a low-priority feature).
        return " " * 4

class _UserSpaceContext(object):
    """
    This class specifies a context manager that
    ensures that items in __builtins__ and sys output streams
    are restored correctly after a user-space evaluation.
    """
    def __enter__(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        self._stdin = sys.stdin

        self._builtins_state = {k: v for k, v in __builtins__.items()}

    def __exit__(self, *args, **kwargs):
        # this part seems weird, and it is,
        # but even though the code is present in the safe_eval template
        # these don't seem to be closed properly:
        sys.stdout.close()
        sys.stderr.close()

        sys.stdout = self._stdout
        sys.stderr = self._stderr
        sys.stdin = self._stdin

        for k, v in self._builtins_state.items():
            __builtins__[k] = v
