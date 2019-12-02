# Samuel Dunn
# CS320, POFIS.
# This setup script manages bundling POFIS into a redistributable wheel.
# (wheel is the python package format)

from setuptools import setup, find_packages
import os
import subprocess
import shutil

# POFIS's version (may want to import this from POFIS
# directly in the future.)
version = '0.0.0b2'

# Dependencies for POFIS runtime.
dependencies = ('cherrypy', 'jinja2')

def find_all_items_in_dir(module, path, filter=None):
    """
    This function generates a list of all items within a directory recursively
    This can be used for setuptools.setup's package_data paramter, which recognizes
    glob notation, but does not recursively append items.

    :param str module: the pythonized representation of a module (ex: pofis.site (instead of pofis/site))
    :param str path: the path to enumerate, it must be nested within module's folder.
    :param callable filter: a function to call to filter out paths. It receives the path relative to `path` of the item being filtered.
        if it returns True, the item is included, False causes the item to be discluded.

    .. note:: only files paths are passed to filter, if a path is a directory it will (eventually) have its contents enumerated.
                so write `filter` to expect this.
    """
    if filter is None:
        filter = lambda p: True # to reduce logic later on.

    data_files = []
    module_path = module.replace('.', os.path.sep)
    real_path = os.path.join(module_path, path)

    for root, dirs, files in os.walk(real_path):
        for f in files:
            p = os.path.join(root.replace(module_path, ''), f)[1:] # the slicing removes a leading path-separator that we don't want
            if filter(p):
                data_files.append(p)

    return data_files

def push_dir(path):
    """
    changes directories to `path`, upon call to pop_dir, restores directory.
    """

    cwd = os.getcwd()
    if not globals().get('!path_stack'):
        globals()['!path_stack'] = []

    path_stack = globals()['!path_stack']

    try:
        os.chdir(path)
    except Exception:
        raise # no need to block the exception, but we need the other functionality of try-blocks.
    else:
        path_stack.append(cwd)

def pop_dir():
    """
    The counterpart to `push_dir`, restores the path the interpreter was previously at prior
    to the most recent call to push_dir.

    :raises: RuntimeError if there is no corresponding prior call to push_dir
    """
    if not globals().get('!path_stack'):
        raise RuntimeError("No prior call to push_dir")

    path_stack = globals()['!path_stack']
    if len(path_stack) == 0:
        raise RuntimeError("all push_dirs have already been popped.")

    os.chdir(path_stack.pop())

class PushedDir(object):
    """
    Convenience context manager to join the functionality of push_dir and pop_dir
    """
    def __init__(self, path):
        self._path = path

    def __enter__(self):
        push_dir(self._path)

    def __exit__(self, *args, **kwargs):
        pop_dir()
        return False

def main():
    # 1) Run sphinx over refdocs
    # For now, we'll just run a sphinx build with every packaging.
    # since we expect refdocs to be the most volatile portion of the project.
    with PushedDir('sphinx'):
        subprocess.call(['make', 'html'])

    # 2) copy refdocs into pofis/site
    # since we're running a new sphinx build every packaging, lets make sure the old sphinx build is
    # cleared out of location.
    try:
        shutil.rmtree(os.path.join('pofis', 'site', 'refdocs'))
    except OSError:
        pass # not a big deal if its not there
    # then copy the new one in.
    shutil.copytree(os.path.join('sphinx', 'build', 'html'), os.path.join('pofis', 'site', 'refdocs'))

    # precompute package_data args (to reduce clutter)
    pofis_site_data = find_all_items_in_dir('pofis.site', 'ace-builds') + find_all_items_in_dir('pofis.site', 'refdocs') +\
                      find_all_items_in_dir('pofis.site', 'styles') + find_all_items_in_dir('pofis.site', 'templates')
    pofis_test_suite_data = find_all_items_in_dir('pofis.test_suite', 'prompt_strings', lambda p: p.endswith('.txt')) + ["*.json"]


    # 3) run setuptools.setup
    setup(
        name='pofis',
        version=version,
        packages=find_packages(),
        author='Abdi Vicenciodelmoral, Andrew Cornish, Becca Daniel, Samuel Dunn',
        # include emails in the future.
        install_requires=dependencies,
        setup_requires=("wheel",),
        entry_points={'console_scripts': ['POFIS_quicklaunch=pofis:main']},
        package_data={'pofis.test_suite': pofis_test_suite_data,
                      'pofis.site': pofis_site_data
        })

    # 4) now that setup is done, we should clean out pofis/site/refdocs so
    # that the development environment seeks out ./sphinx/build/html instead (for dev convenience.)
    # There's probably a better way to bundle the data than to copy it, then delete it, but w/e. This works.
    shutil.rmtree(os.path.join('pofis', 'site', 'refdocs'))

if __name__ == "__main__":
    main()