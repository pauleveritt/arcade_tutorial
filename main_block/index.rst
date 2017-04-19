==========
Main Block
==========

One more bit of housekeeping before we get into writing our game. Let's
make a "main block" for the startup of our program.

.. youtube:: 2wndmmo2sCE

Steps
=====

#. Move the ``print`` function inside an ``if`` statement:

   .. literalinclude:: game.py
        :language: python
        :linenos:

#. Run the program, this time by clicking the green arrow in the
   left margin of line 3 (the ``if`` statement) and selecting ``Run``.

What's Going On
===============

Let's be clear up front: it's ok to memorize this and do it, rather than
learn the little details.

In Python, some files are meant for "import" into other files, but not
for being run directly. Why does this matter? When imported into another
file, you might not want to directly run some stuff. Imagine if every file
started its own game...you'd have windows open everywhere.

To fix this, Python programmers arrange for there files to know when
the file is being included in another main file, or when the file is being
executed directly. We call this the "main block".

The ``if`` statement is how Python checks to see if something is true. In
this case, the ``if statement`` looks to see if ``__name__`` is equal to
the value ``__main__``. What is ``__name__``? It's a special variable
Python assigns when the file is directly executed, instead of imported.

Here is a
`good explanation <http://stackoverflow.com/questions/419163/what-does-if-name-main-do>`_
of what Python is doing with the main block.

Terms Used
==========

- *if statement*. Maybe you want some code to run when in one situation but
  not another. Python's *if* statement lets you specific a condition.

- *Main block*. A standard, safe way to let the same file be either directly
  executed or imported into another main file.
