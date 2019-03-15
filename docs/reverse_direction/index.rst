=================
Reverse Direction
=================

Detect *when we hit the right edge* then *reverse direction*.

Code
====

.. literalinclude:: game.py
    :emphasize-lines: 10,11, 20-25

Analysis
========

#. We put the *starting position* at 10.

#. We introduce concept of *velocity* in the constructor.

#. Velocity is two things:

   - How *fast* we are moving

   - Which *direction* we are moving

   - A *negative* number means we are moving that fast, *backwards*

   - *Note: This number is a LOT bigger for Arcade 2.0*

#. *No changes* to ``on_draw``...shows the point that we change the data
   and let the drawing take care of itself.

#. Important changes in ``update``

#. On each tick, move ``self.position`` (really, ``center_x``) based on:

    - Velocity

    - ``delta_time`` meaning, how long since we were last called

    - Makes sense

#. Introduce a conditional, aka the ``if``

#. How do we know if we are at the right edge?

    - The right edge is a certain number of pixels from the *origin*

    - The number is...the *window width*

    - We care about the *edge* of the circle, not the center

    - So we have to use the *radius*

    - If ``center + radius`` is at the edge, turn around

#. How do we turn around? Change the *velocity* to reverse.

Exercises
=========

#. Try making the circle bigger. Does the formula still work?

#. Same for the window width.

Analysis
========

#. We could have skipped a separate line for ``is_at_right`` and just done
   that formula in the ``if``. What are some reasons for doing it
   separately?
