# Samuel Dunn
# CS 320, Fall 2019
# This files makes the `pofis` directory a python module.

def main():
    """
    Launches the cherrypy server and hosts the refdocs and interactive portions of POFIS.
    """
    import cherrypy
    import os
    from .site import Root, get_cherrypy_config

    cherrypy.tree.mount(Root(), '/', config=get_cherrypy_config())
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})

    # for development purposes there are a few extra files
    # we want cherrypy to autoreload when changed:
    tutorial_data = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'tutorial', 'tutorial_data.json')

    cherrypy.engine.autoreload.files.add(tutorial_data)

    cherrypy.engine.start()
    cherrypy.engine.block()

