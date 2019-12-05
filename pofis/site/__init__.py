# Samuel Dunn
# CS 320, Fall 2019

# This module defines all purely-site based functionality for POFIS

import os
import cherrypy

# aggregate top level entities from submodules.
from .root import Root
from .refdoc_compat import find_refdoc_dir
from ..auth import Authenticator


# Lets go ahead and define the config dict and related helper functions here:
def get_cherrypy_config():
    """
    Returns a config dict suitable to pass to cherrypy at tree-mount-time
    """
    cp_conf = {
        '/' : {
        },
        '/login' : {
            'tools.auth_basic.on': True,
            'tools.auth_basic.realm': 'pofis',
            'tools.auth_basic.checkpassword': Authenticator().cp_authenticate,
            'tools.auth_basic.accept_charset': 'UTF-8'},
        '/suites' : {
            'tools.auth_basic.on': True,
            'tools.auth_basic.realm': 'pofis',
            'tools.auth_basic.checkpassword': Authenticator().cp_authenticate,
            'tools.auth_basic.accept_charset': 'UTF-8'
        },
        '/refdocs' : {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': find_refdoc_dir(),
            'tools.staticdir.index': 'index.html'
        },
        '/styles': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': get_styles_dir()
        },
        '/ace': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': get_ace_dir()
        }
    }
    return cp_conf

def get_styles_dir():
    """
    locates the site's style directory.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, 'styles')

def get_ace_dir():
    """
    Locates and returns the ACE project directory.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, 'ace-builds', 'src-noconflict')