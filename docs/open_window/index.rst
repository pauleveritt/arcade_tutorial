===========
Open Window
===========

Here we go, let's write a game. Starting with...opening a window on
the screen where our game will live.

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/j2-EEguhwfU"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

Code
====

.. literalinclude:: game.py

#. Click the green arrow on line 3 and choose ``Run``.

#. A new window appears. It's our game!

#. Close the window.

Analysis
========

- We used two functions *imported* from arcade

- ``open_window`` is a function which takes 3 arguments

- ``run`` is a function that tells Arcade "ready to go"

Exercises
=========

#. Change the arguments to ``open_window``, putting the string
   first. What goes wrong?

#. Use ``Ctrl-B`` to navigate to the implementation of
   ``open_Window`` and see why this fails.

#. Close that tab, put your cursor inside ``open_window``, and
   hit ``Ctrl-P``. This is a *less-disruptive* way to expore.

#. What happens if you open a window too big for the screen?

#. Instead of importing arcade then doing ``arcade.open_window``,
   change to the ``from blahblah import blahblah, blahblah``
   syntax.

Quiz
====

#. What is the name of the function which takes arguments?

#. What is the data type of that function's third argument?

