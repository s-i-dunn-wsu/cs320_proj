Syntax
=========
.. author: Becca Daniel

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indentation
------------------------
**Tabs or Spaces:**
Python considers leading white space as Syntax.
You can use tabs or spaces throughout your program but you must be consistent.

Per PEP 8 Style Guides, Spaces are the preferred indentation method.

Anytime a line ends in a colon : the next line requires an indentation

.. code-block:: python

    def my_function(food):
        for x in food:
            print(x)


Comments
--------------
Lines that start with a # are comments and ignored by Python

.. code-block:: python

    # this is a comment

For multiple line comments, PEP 8 suggests using multiple hash marks #

.. code-block:: python

    # this is a comment
    # this is another comment
    # all of these will be ignored by Python

`Commenting Guide`_

Data Types
-------------------
In Python you are not required to specify the data type of your variables.

Naming Variables
-------------------
- Can only contain alphanumeric characters (a-z, A-Z, 0-9, underscores)
- Can only start with a letter or an underscore, not numbers
- Are case sensitive

.. code-block:: python

    variableName = 1;
    variable_name = "String";
    variable_name2 = 'String';
    variableName3 = 4.5;
    _variable = [1, 2, 3, 4];

See Also
-----------

.. links to pages within POFIS


External References
---------------------
.. _`Commenting Guide`: https://realpython.com/python-comments-guide/
.. links to sources outside of POFIS

