=========
Left Edge
=========

Reverse direction if we hit the left edge

Code
====

.. literalinclude:: game.py
    :emphasize-lines: 27-30

Analysis
========

#. The "algoritm" (logic to make the decision) is easier on the left.

#. Why? It's just *zero*, no screen width.

Exercises
=========

#. Both conditionals (the ``if`` statements) result in the same action.
   Combine them. *Hint: combine with ``or`` and group each condition in