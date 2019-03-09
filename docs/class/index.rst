===========
First Class
===========

Start using a Python class to organize the game.

Code
====

.. literalinclude:: game.py

Analysis
========

- We make a *class* for our game, with a class name of ``MyGame``

- This class is a "recipe" for the game, not an *actual running game*

- To make an actual game, we make an *instance* of the game on line 14

- Our class doesn't start with an empty slate, it uses ``arcade.Window``
  as a starting point

- This is called *subclassing*, and ``MyGame`` is a "subclass" of
  the ``arcade.Window`` class (aka superclass, base class)

- ``arcade.Window`` is itself a subclass of ``pyglet.window.Window``
  which has a LOT of complexity

- But *our* game doesn't have to do all that, it is using the base
  classes as a starting point

- Classes can hold data (called state) and behavior (called methods)

- When a function is part of a class, it is called a *method*

- It is easy to spot a method in Python: it is a ``def`` with a first
  argument of ``self``

- What is "self"? A variable hold the *instance* of the class that we
  are working on

- In Arcade, when you use a class instead of a function, the Arcade
  rules are different. For example, ``on_draw`` has a ``start_render``
  but not a ``finish_render``. Arcade knows to run ``finish_render``.

Exercises
=========

#. Put a breakpoint just after making the ``game`` instance, run the game
   under the debugger, and see what data is stored on the instance.

#.

Quiz
====

- What is a superclass used for?

- What are the differences between a function and a method?

- What is the difference between a class and an instance?

- In a method, the first argument (``self``) hold what value?