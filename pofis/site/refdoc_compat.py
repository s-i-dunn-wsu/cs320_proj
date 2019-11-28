# Samuel Dunn
# CS 320, Fall 2019
# This module supplies tools for finding and accessing the refdocs compiled by sphinx.

import os

def find_refdoc_dir():
    """
    Returns the absolute path to wherever the refdocs are located.
    """
    # the refdocs are in one of two places:
    # in the same folder as here, as part of the installation
    # or a few directories up nested in the project root (in a dev environment.)

    # Always prefer the installed path to the dev path (for security reasons)

    here = os.path.dirname(os.path.abspath(__file__)) # the directory containing this file.

    installed_refdoc_path = os.path.join(here, 'refdocs')

    if os.path.exists(installed_refdoc_path) and os.path.isdir(installed_refdoc_path):
        return installed_refdoc_path

    # look a few directories up for a 'sphinx/build/html' folder
    proj_root = os.path.abspath(os.path.join(here, '..', '..'))
    sphinx_build_root = os.path.join(proj_root, 'sphinx', 'build', 'html')

    if os.path.exists(sphinx_build_root) and os.path.isdir(sphinx_build_root):
        return sphinx_build_root

    raise RuntimeError("Unable to locate suitable refdoc folder.")