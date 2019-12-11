Functions
==========

Difference between function and method. Info found at:
https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function

A **function** is a piece of code that is called by name. It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed.

A **method** is a piece of code that is called by a name that is associated with an object. In most respects it is identical to a function except for two key differences:

1. A method is implicitly passed to the object on which it was called.
2. A method is able to operate on data that is contained within the class (remembering that an object is an instance of a class - the class is the definition, the object is an instance of that data).



Everything below is from https://www.w3schools.com/python/default.asp

Definition
-----------
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.


Creating a Function
--------------------
In Python a function is defined using the def keyword:

.. code-block:: python

    def my_function():
        print("Hello from a function")




Calling a Function
-------------------
To call a function, use the function name followed by parenthesis:

.. code-block:: python

    def my_function():
         print("Hello from a function")

    my_function()


    C:\Users\My Name>python demo_function.py
    Hello from a function


Parameters
-----------
Information can be passed to functions as parameter.

Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

The following example has a function with one parameter (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

.. code-block:: python

    def my_function(fname):
        print(fname + " Refsnes")

    my_function("Emil")
    my_function("Tobias")
    my_function("Linus")


    C:\Users\My Name>python demo_function_param.py
    Emil Refsnes
    Tobias Refsnes
    Linus Refsnes








Default Parameter Value
------------------------
The following example shows how to use a default parameter value.

If we call the function without parameter, it uses the default value:

.. code-block:: python

    def my_function(country = "Norway"):
        print("I am from " + country)

        my_function("Sweden")
        my_function("India")
        my_function()
        my_function("Brazil")

    C:\Users\My Name>python demo_function_param2.py
    I am from Sweden
    I am from India
    I am from Norway
    I am from Brazil


Passing a List as a Parameter
------------------------------
You can send any data types as a parameter for a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as a parameter, it will still be a List when it reaches the function:

.. code-block:: python

    def my_function(food):
        for x in food:
            print(x)

    fruits = ["apple", "banana", "cherry"]

    my_function(fruits)


    C:\Users\My Name>python demo_function_param3.py
    apple
    banana
    Cherry


Return Values
--------------
To let a function return a value, use the return statement:

.. code-block:: python

    def my_function(x):
        return 5 * x

    print(my_function(3))
    print(my_function(5))
    print(my_function(9))


    C:\Users\My Name>python demo_function_return.py
    15
    25
    45


Keyword Arguments
------------------
You can also send arguments with the key = value syntax.

This way the order of the arguments doesn’t matter.

.. code-block:: python

    def my_function(child3, child2, child1):
        print("The youngest child is " + child3)

    my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


    C:\Users\My Name>python demo_function_kwargs.py
    The youngest child is Linus




Arbitrary Arguments
--------------------
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

.. code-block:: python

    def my_function(*kids):
        print("The youngest child is " + kids[2])

    my_function("Emil", "Tobias", "Linus")


    C:\Users\My Name>python demo_function_kwargs.py
    The youngest child is Linus


Citations
----------

https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function

https://www.w3schools.com/python/default.asp


Tutorial
----------------

Please see our guided tutorial for this content here: tutorial_

.. _tutorial: /tutorials/take_tutorial?tutorial_num=2
