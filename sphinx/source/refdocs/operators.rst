Operators
==========

.. author: Python Boot camp

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Assignment Operators
---------------------

Used to assign values to variables



+-------------+------------+----------------+
| operator    | example    |  equivalent to |
+=============+============+================+
| =           |   = 5      |   x = 5        |
+-------------+------------+----------------+
| /=          |  x /= 3    |   x = x / 3    |
+-------------+------------+----------------+
| %=          |  x %= 3    |   x = x % 3    |
+-------------+------------+----------------+
| +=          |  x += 3    |   x = x + 3    |
+-------------+------------+----------------+
| -=          |  x -= 3    |   x = x - 3    |   
+-------------+------------+----------------+
| \*=         |  x \*= 3   |   x = x \* 3   |
+-------------+------------+----------------+




Comparison Operators
---------------------

+-------------+--------------------------+--------------------+
| operator    |         meaning          |       example      |
+=============+==========================+====================+
|  ==         | equal to                 | # 5 == 3 is false  |
+-------------+--------------------------+--------------------+
|  !=         | not equal to             | # 5 != 3 is true   |
+-------------+--------------------------+--------------------+
|  >          | greater than             | # 5 > 3 is true    |
+-------------+--------------------------+--------------------+
|  <          | less than                | # 5 < 3 is false   |
+-------------+--------------------------+--------------------+
|  >=         | greater than or equal to | # 5 >= 3 is true   |
+-------------+--------------------------+--------------------+
|  <=         | less than or equal to    | # 5 <= 3 is false  |
+-------------+--------------------------+--------------------+

Logical Operators
------------------

Used to combine conditional statements:

and - all statements need to be true to return True.

.. code-block:: python

    if x < 5 and x > 1: # only runs if x less than 5 and more than 1

or - all statements need to be false to evaluate to False.

.. code-block:: python

    if x >= 2 or y <= 2: # returns True if one of these is true

not - switches the truth value.

.. code-block:: python

    if not(x < 5 and x > 1):  # if x between 1 and 5, returns False


Identity Operators
-------------------

Used to compare objects. Not checking if they are equal, but if they are actually the same object,
 with the same memory location:

.. code-block:: python

    is                 # Returns True if both variables are the same object

    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x

    print(x == y)        # This comparison returns True because content of x is equal to content of y
    print(x is y)            # False because x is not the same object as y
    print(x is z)            # Returns True because z is the same object as x
    
    is not                # Returns true if both variables are not the same object    


