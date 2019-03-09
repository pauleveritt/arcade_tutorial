========================
Using Class Constructors
========================

Using a class is like using a cookie recipe. Sometimes you want your
instance -- the cookie -- to be setup in a certain way, such as number
of chocolate chips.

The class *constructor* lets you write the code for "constructing" the
instance, to get it into the right starting point.

Code
====

.. literalinclude:: game.py

Analysis
========

- Classes can have "constructors"

- A constructor is a *method* with a special name -- ``__init__``

- Like all method, it takes ``self`` as a first argument (``self``
  is the particular instance being constructed)

- Like all methods, you can pass arguments to the constructor to use
  in the construction

- Setting the bg color is conceptually part of "construction"

- No need for GAME_TITLE as a constant

- Instead, use the *instance* to store the title as an *instance attribute*

- 'self.' is a way to refer to the instance ("self") and store a variable on it

- Thus, 'self.title' means: "Store a value for ``title`` on the instance"

- Your superclass (e.g. ``arcade.window``) might also have a constructor,
  so you might have to call that one with ``super()``

Exercises
=========

#. Comment out the line that calls the superclass constructor. What does
   PyCharm tell you?

#. Make the background color something each instance can vary on:

    - Add ``bgcolor`` to the constructor arguments, just like ``title``

    - Store it on the ``self``, just like ``title``

    - Use the instance value in ``set_background_color``, just like we
      used title in ``draw_text``

#. Do the same for font size.

#. In the constructor, add "message = 'Hello'" then add ``print(message)`` in
   the ``on_draw`` method. What happens?

Quiz
====

#. Is the constructor used to construct classes or to construct instances?

#. Is ``__init__`` a function or a method?

#. On what line is the constructor called (i.e. executed)?