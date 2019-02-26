=======================
Functions and Arguments
=======================

Going to a hostess and saying "I want a seat" is like calling a function.
But the hostess needs more information to seat you (run the function).
She needs to know how many to seat.

You could provide that information when running the function: "I need
a seat for 2." You're *running the function with an input value*.

We call those function *arguments*.

Let's write our *own function*, one that needs an argument.

Code
====

.. literalinclude:: game.py

Analysis
========

- We wrote our own function by using the ``def`` keyword (short
  for *define*)

- Our function *name* is ``print_version``

- Our function takes 1 *argument*

- Meaning, anybody who *calls* our function, has to call it with
  a value

- Our function takes that *value* and makes a *variable* with the
  *name* of ``this_version``

- Our function then uses that *local* variable to do some work

Exercises
=========

#. Call the function without any arguments.

#. Call the function by *passing it* an integer instead of a string.

#. Try printing ``this_version`` at the end of the program.

Quiz
====

#. Can ``print_version`` be used in other files? If so, how?

#. What does this function *return*?