========================
Set the Background Color
========================

Games have colors, including a background color. Arcade makes it really
easy to set the background color, so let's do so.

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/AXhYJSO5oIc"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

Steps
=====

What's Going On
===============

We changed the title of our window, aka the "Window Title", to
"Coin Game". That's the name of the game we're making.

Line 5 is the main change. We are again calling a Python function that
is in the Arcade package. This function, ``set_background_color``, takes
one function argument...the color we want to use.

Computer color schemes are usually defined with numbers or letters, which
are hard to remember. Arcade makes this easier with some predefined colors
that have easy names. These are all done as variables, each available
inside the ``arcade.color`` variable. We chose ``WHEAT``.

As we have seen, Arcade has a lot of functions and variables that can help
us.

And yet, after all of this, the background color did not change. What went
wrong? We have one more thing to learn from Arcade, which we'll see in the
next step.
