===============
Handle Keypress
===============

First event handler, keypress reverses direction.

Code
====

.. literalinclude:: game.py
    :emphasize-lines: 14-15, 25-29, 31-33

Analysis
========

#. We make a method ``reverse`` that let's us do the work for reversing
   without thinking much about it.

#. Combine the two tests -- right edge and left edge -- into *one* ``if``

#. Add a method ``on_key_press``, which Arcade calls whenever a key is
   pressed

#. This method is known as a *handler*...it handles *events*

#. Arcade passes information from the event, into this this method, as
   *arguments*

#. You can use this to decide *which key* was pressed.

Exercises
=========

#. Add an ``else`` that prints information about what key was pressed
   when it was *not* one of those two keys.

#. No need for left or right...just have *spacebar* perform a reverse.
