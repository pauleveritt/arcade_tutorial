===========
Open Window
===========

Here we go, let's write a game. Starting with...opening a window on
the screen where our game will live.

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/j2-EEguhwfU"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

Steps
=====

#. Change the main block to have two lines that use Arcade:

   .. literalinclude:: game.py
        :language: python
        :linenos:

#. Click the green arrow on line 3 and choose ``Run``.

#. A new window appears. It's our game!

#. Close the window.

What's Going On
===============

The 'open_window' and 'run' are functions in the 'arcade' package. We can
tell they are functions because they have parenthesis () where we "call"
the function.

A function is just a bunch of lines of programming, organized with a name.

Some functions can just be called, e.g. run().

Other functions need some variables handed to them. We call these
variables "function *arguments*."

The 'open_window' function takes 3 "arguments".

How can we tell what arguments to provide when calling a function?
When you get in the parenthesis, PyCharm will tell you a little bit.
But even better, press F1 when the cursor is on 'open_window', and
PyCharm gives you information about these arguments, plus some
documentation.
