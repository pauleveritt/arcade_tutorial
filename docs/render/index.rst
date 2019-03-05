=================
Start/Stop Render
=================

Get Arcade to actually do some of the drawing commands that
we issue by calling ``start_render`` and ``finish_render``.

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/DcC1dyHMwl0"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

Code
====

.. literalinclude:: game.py

Analysis
========

- Arcade has a simple drawing mode (functions) and a richer game
  way of writing code (classes)

- We are still using the simple drawing functions

- Which means, we need to tell Arcade when we start sending drawing
  commands and when we stop

- The background color isn't set until we draw on the screen

- In arcade, we do our drawing between the 'start_render' and
  'finish_render' functions

- These functions take no arguments

- Again, let PyCharm do the autocomplete with you

Exercises
=========

#. Try commenting out ``start_render``, ``finish_render``, and
   both.
