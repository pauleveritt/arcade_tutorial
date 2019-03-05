========================
Set the Background Color
========================

Games have colors, including a background color. Arcade makes it really
easy to set the background color, so let's do so.

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/AXhYJSO5oIc"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

Code
====

.. literalinclude:: game.py

Analysis
========

- We changed the *title* of our window

- We added a call to ``set_background_color``

- Names such as ``WHEAT`` are called *constants*. In Python,
  constants are noted with *all caps*.

- Arcade's names for colors are really just RGB *tuples*

- Running this does *not* yet change the background color

Exercises
=========

#. Use ``Ctrl-B`` to navigate to the definition of ``WHEAT``
   and tell its RGB value.

Quiz
====

#. What is a tuple?

#. Can you change a value in a tuple?

#. How can you tell that a variable is intended to be used as
   a constant?

#. In *Python*, can you change the value of a constant?

#. Why doesn't the background color change?