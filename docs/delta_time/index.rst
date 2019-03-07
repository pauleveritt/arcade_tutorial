==========
Delta Time
==========

Code
====

.. literalinclude:: game.py

Analysis
========

- The previous example left 'delta_time' unexplained

- 'arcade.schedule' runs our 'on_draw' function every 1/2 second

- But it might not be exactly half a second...if your computer is
  bogged down, or the game gets laggy, it might get behind

- So arcade.schedule keeps track of how long it has been since the
  last time your function was called

- It passes this value to your function as the first argument

- We change our text to include the value of this argument, so we get
  a better sense
