======================
Classes and Delta Time
======================

Re-implement the earlier "delta time" section, this time with classes.

Code
====

.. literalinclude:: game.py

Analysis
========

#. Instead of ``arcade.schedule``, we use a method called ``update``

#. Arcade calls this method every tick

#. We add another *instance attribute* named ``self.position``

#. This is the *x coordinate* for the text

#. Every "frame", we *change the value of the position*, then redraw

#. This makes the *text move*

#. Like ``on_draw``, ``arcade.Window`` has a special method ``update``

#. Unlike drawing, this is for working on your game data

#. That's the *workflow* -- modify the game data, then on the next "tick",
   redraw

#. We also show how to change an instance *attribute*, ``game.position = 10``

Exercises
=========

#. Have the initial starting position be 20 instead of 10.


#. Move by 5 pixels on each animation instead of 1.


Quiz
====

