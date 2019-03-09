===============
Class Animation
===============

Re-create the earlier "kinda not-really" animation section, this time with
a class.

Code
====

.. literalinclude:: game.py

Analysis
========

#. This time we *pass another value* into the constructor and store it
   on the *instance*.

#. We are now storing *width and height* on the instance.

#. Why? We are doing a *calculation* in ``on_draw``. We want to draw the
   text in the middle of the screen. ``width`` and ``height`` were
   passed into the constructor but to be used in *another* method, need
   to be stored on the instance ``self``.

What Is ``on_draw``?
====================

Arcade makes it easy to do games. You write a method named ``on_draw`` and
Arcade will *call* that method to do all the drawing.

Exercises
=========

#. Put the text a third of the way from the top.

