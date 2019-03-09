=========
Animation
=========

.. raw:: html

  <iframe width="640" height="360"
    src="https://www.youtube.com/embed/yzC2TwhER0c"
    frameborder="0" allowfullscreen="1">&nbsp;</iframe>

Introduction to animation and scheduling with a drawing function.

Code
====

.. literalinclude:: game.py

Analysis
========

- We moved our drawing into a second function, named 'on_draw'

- Our 'main' function now does the basics (make a window, set up
  drawing, and run)

- However, we introduce a BIG new idea: arcade.schedule

- This is a function in the arcade package

- Schedule runs a unit of work (the first argument) every X
  seconds (the second argument)

- In our case, we tell arcade to run our 'on_draw' function every
  1/2 second

- This is the basis of animation

- Because of how arcade does animation, with arcade.schedule, you
  need start_render but we no longer need finish_render

Exercises
=========

#. Change the ``schedule`` function to run much more *frequently*.

#. Change ``draw_text`` to "accidentally" draw most of the text outside
   of the window.

#. Use Python's ``random.choice`` and ``range`` to randomly choose an
   X position between 100 and 400.

Quiz
====

#. What is ``delta_time`` and what is it used for?

#. In this step, is ``delta_time`` used?

#. In this step, is it useful to have window height/width as constants
   at the top?