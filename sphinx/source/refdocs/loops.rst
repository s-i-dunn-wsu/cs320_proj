Loops
====================
A loop statement allows us to execute a statement or group of statements multiple times. Python offers a variety of constructs to do such executions.

For Loops
------------
'For' loops are traditionally used when you have a block of code which you want to repeat a fixed number of times.

Syntax of for Loop
--------------------
.. code-block:: python

    for var in iterable:
	Statement...


The **Statement** in the loop body are denoted by indentation, as with all Python control structures, and are executed once for each item in
**iterable**. The loop variable **var** takes on the value of the next element in **iterable** each time through the loop.

.. code-block:: python

    a = ['foo', 'bar', 'baz']
    for i in a:
        print(i)


While Loops
-------------
With the while loop we can execute a set of statements as long as a prefined condition is true.

Syntax for While Loop
------------------------
.. code-block:: python

    while condition:
    statements

As long as the "condition" is complied with all the statements in the body of the **while** loop are executed at least once. After each time the statements are
executed, the condition is re-evaluated.

.. code-block:: python

    a= ["foo", "bar", "baz"]
    position = 0
    while position < len(fruits):
        print(fruits[position])
        position = position + 1

    print("reached end of list")




Loop Control Statements
-----------------------------
Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.


Python supports the following control statements:

- **break**: Terminates the loop statement and transfers execution to the statement immediately following the loop.
- **continue**: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
- **pass**: The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

Citations
----------
https://www.tutorialspoint.com/python/python_loops.htm
https://wiki.python.org/moin/ForLoop


Tutorial
----------------

Please see our guided tutorial for this content here: tutorial_

.. _tutorial: /tutorials/take_tutorial?tutorial_num=3
