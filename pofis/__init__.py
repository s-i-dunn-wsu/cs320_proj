# Samuel Dunn
# CS 320, Fall 2019
# This files makes the `pofis` directory a python module.

def main():
    """
    Launches the cherrypy server and hosts the refdocs and interactive portions of POFIS.
    """
    import cherrypy
    from .site import Root, get_cherrypy_config

    cherrypy.tree.mount(Root(), '/', config=get_cherrypy_config())
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.engine.start()
    cherrypy.engine.block()

