Prototypical Object Oriented Programming
=========================================

What you should know already
----------------------------

What is OOP?
-------------

At a surface level, object oriented programming is a programming paradigm
that treats data as an entity. In this paradigm data isn't merely a state captured by bits, but
rather an *object* which has a state, or `attributes`, and a set of actions, or `methods`.
An object can have its attributes modified, and it can have its methods invoked.

Consider a hammer, a hammer isn't simply a hunk of wood and a metal head. It has
an intended purpose alongside its form.

In OOP, a hammer would be represented with attributes that reflect its composition,
and a set of methods that define a hammers use.

At its simplist level, OOP may seem like syntactic sugar - especially coming from a C
background. But several other paradigms arise from the OOP mentality which really
highlight its power. Please see the 'See Also' section for more information.

Common Features
----------------

In Python
-----------

Clasical vs Prototypical
-------------------------

.. warn::
    This is an advanced topic.

There are two different types of OOP, classic and prototype.
The primary differences between the two are:

    - what an object is in memory
    - what a class is at runtime.

In Classical OOP an objects state is strictly limited by its inherited classes.
All of its classes define a finite amount of attributes, and the compiler
will know the arrangement of those attributes in memory. At runtime attributes
are resolved as off sets from the base address of the object. Put simply,
the set of attributes (but not their current state) of an object at runtime is
rigid.

In Prototypical OOP things are a little different. Object attributes
are flexible at runtime. You can append attributes to an object instance at any point.

Consider the following:

Lets assume there's a class that defines exactly 2 integer attributes, `x`, and `y`.
In both these examples let `obj` be an instance of this class.

Clasical:
.. code-block::
    :lineno:

    obj.x = 5; // pass: obj has attribute x.
    obj.y = 0; // pass: obj has attribute y.
    obj.z = -1; // fail: obj does not have a z attribute

Prototypical:
.. code-block::
    :lineno:

    obj.x = 5; // pass
    obj.y = 0; // pass
    obj.z = -1; // pass: the instance `obj` gains the attribute `z`.

Other generalities:

Prototypical languages will often also be:
    - interpreted
    - dynamically typed

Classic languages will often also be:
    - compiled
    - statically typed.



See Also
---------
.. inheritance
.. polymorphism
.. duck typing

External Resources
------------------

.. link wiki articles for classic v prototype