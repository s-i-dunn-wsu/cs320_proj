Generators
============

.. Becca

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Motivation
------------

Generators are defined just like any normal function but they require the use of the keyword yield. These functions work on iterator objects and behave like an iterator. 


Local States
----------------

The use of yield allows generators to save the state of its local variables and “pauses” between use next() call

The code below, yields 1 then 2 with each call to next(). It then waits, saving its state in memory.

.. code-block:: python

    def numberGen(n):
        number = 1
        while number < n:
            yield number
            number += 1

    myGenerator = numberGen(3)
    print(next(myGenerator))
    print(next(myGenerator))


Loop examples
----------------
Each time you loop through a generator, it requires a new generator 
object to be created to be used again. Both loops below have the same output.

.. code-block:: python

    def numberGenerator(n):
        number = 0
        while number < n:
            yield number
            number += 1

    for i in numberGenerator(10):
        print(i)

    myGenerator = numberGenerator(10)
    counter = 0;
    while counter < 10:
        print(next(myGenerator))
        counter += 1

See Also
-----------

.. links to pages within POFIS
