Importing in Python
=====================

.. author: Samuel Dunn

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Read before:
-------------

Being familiar with topics presented in the following
will help you suceed in understanding these topics.

- :doc:`Prototypical Object Oriented Programming<./prototypical_oop>`


At a glance
-------------
Many languages use a directive of some kind in order to bridge functionality
provided in different source files. In Python, this is the `import` keyword.


How It works
-------------
Recall that *everything* in python is an object. This includes modules and packages.
A module is a python-recognized folder, or a .py file. `import` will access
a module and load it into the local namespace. Once the module is imported
its usable like any other object, you can access its members,


Syntax
--------

Examples
---------

Let's image a module, `foo`, with a single submodule `bar`.

Direct import
.............

.. code-block:: python

    import foo # imports just foo


Renamed import
..............

.. code-block:: python

    import foo as new_name # foo is available locally as new_name

This can be done with any type of import.

Submodule import
.................

.. code-block:: python

    import foo.bar # the bar module is available via foo as foo.bar

Extracted import
................

When importing you can use the `from` keyword to
extract a particular object from the supplied module.

.. code-block:: python

    from foo import bar # bar module is available as bar.

This works for any object within the module supplied to
the `from` keyword.

For example, lets suppose that the `foo` module has a function in it
called `func`. We can directly import `func` like so:

.. code-block:: python

    from foo import func # note: you could use 'as' to rename func here.


What happens when import is used?
---------------------------------
`Python Import Documentation`_

The common "gotcha's"
-----------------------

-   Just because a module is a submodule does not mean its implicitly available
    within the parent modules namespace.

    For example, again using foo and bar, if foo does not import bar
    then:

    .. code-block:: python

        import foo # have foo

        # Try to access bar via foo
        foo.bar     # Doesn't work, foo does not have attribute bar.

        import foo.bar # now have foo.bar.

        foo.bar # works now

    This is because the bar module is not loaded simply because foo is.
    Put another way, there is no `bar` object in foo. If foo imports bar
    then we could use it by just importing foo.


Relative imports
-----------------

Like many languages, python has a concept of packages, or collections of modules.
Packages allow for relative imports

Lets give foo another module called baz.

The code from baz could access bar and func like so:

.. code-block:: python

    from . import bar # imports bar
    from . import func # imports func from foo.

    # if bar had something we wanted to import, such as func2
    from .bar import func2


Parallels in other languages:
-----------------------------

+----------+-----------+---------------+----------------------------------------------------------------+
| Language | Directive | Similarities  |  Differences                                                   |
+==========+===========+===============+================================================================+
| C/C++    | `#include`| conceptually  | `#include` expands                                             |
|          |           | similar. Both | as the contents of the                                         |
|          |           | serve to join | contents of the included file.                                 |
|          |           | files.        | Whereas `import` loads the module object into local namespace. |
+----------+-----------+---------------+----------------------------------------------------------------+
| Java     |           |               |                                                                |
+----------+-----------+---------------+----------------------------------------------------------------+


External References
--------------------
.. _`Python Import Documentation`: https://docs.python.org/3.8/library/importlib.html#module-importlib