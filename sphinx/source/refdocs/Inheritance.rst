Inheritance
====================

Inheritance is a feature in object oriented programming, which allows the us to define a class that inherits all the methods and properties from another class.

The class from which a class inherits is called the **base class** or superclass. A class which inherits from a base class is called a **derived class** or subclass. 
Base classes are sometimes called ancestors as well. There exists a hierarchy relationship between classes. It's similar to relationships or categorizations that we know from real life. 
Think about vehicles, for example. Bikes, cars, buses and trucks are vehicles. Pick-ups, vans, sports cars, convertibles and estate cars are all cars and by being cars they are vehicles as well. 
We could implement a vehicle class in Python, which might have methods like accelerate and brake. Cars, Buses and Trucks and Bikes can be implemented as derived classes which will inherit these methods from vehicle.

Base Classes
--------------
Base or parent classes create a pattern out of which child or subclasses can be based on. Parent classes allow us to create child classes through inheritance without having to write the same code over again each time. 
Any class can be made into a parent class, so they are each fully functional classes in their own right, rather than just templates.

Creating a Base Class
-----------------------
.. code-block:: python

    class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires


The code above creates a class called Vehicle, which will act as the base class. 


Derived Classes
-----------------------
Derived or chile class are classes that will inherit from the base class. That means that each child class will be able to make use of the methods and variables of the parent class.


Creating a Derived Class
---------------------------
.. code-block:: python

    class Car(Vehicle):
	pass


    x = Car('white','4','round')
    print(x.color)



With derived classes, we can choose to add more methods, override existing parent methods, or simply accept the default parent methods with the **pass** keyword.

Method Overrriding
-----------------------
Method overriding is a concept of object oriented programming that allows us to change the implementation of a function in the derived class that is defined in the base class. 
It is the ability of a derived class to change the implementation of any method which is already provided by one of its base class.

Overide a method
--------------------
.. code-block:: python

    class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        
    def accelerate(self):
        print('Accelerate Normal')
        



    class Car(Vehicle):
	def accelerate(self):
	    print('Accelerate Fast')
    
	x = Car('white','4','round')

    x.accelerate()


The method accelerates() now prints a different string than the one in the Vehicle base class for this specific instantiation of the class.


Citations
---------------

https://python101.pythonlibrary.org/chapter11_classes.html

https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3