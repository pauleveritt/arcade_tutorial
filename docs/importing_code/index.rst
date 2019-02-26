==============
Importing Code
==============

We're *writing a program*. We don't want to *write everything*. Sometimes
we want to *re-use* a function:

- Something *we* wrote

- Something the *Python install* includes

- Something *somebody published* (like...Arcade)

We need to grab that code and make it part of our current file,
*as if it were typed in directly*.

In Python we use ``import`` to bring in code from somewhere else.

Code
====

.. literalinclude:: game.py

Analysis
========

- Arcade is a *package* that we installed

- It has, in the top level, a *variable* ``VERSION``

- When we ``import arcade``, we have access to everything in ``arcade``

- *But* we have to put ``arcade.`` in front of everything we want

- We could instead get *just* that variable with ``from arcade import VERSION``

Exercises
=========

#. Make the change to do the last part

#. Use put the cursor on ``VERSION`` and use ``Ctrl-B`` to navigate to where
   that variable is *defined*

#. Import one of the drawing functions from ``arcade`` and print it (Hint: type
   ``dra`` and let PyCharm autocomplete

#. Once you did that:

    - Delete the line importing that drawing function

    - Put your cursor on the name in the ``print()``, which now has a
      red squiggly

    - ``Alt-Enter`` to let PyCharm generate the import

#. Set a breakpoint (red circle) beside the ``print()``. Run under the
   debugger, then expand ``arcade`` under ``Special Variables``. See that
   it says it is a "module" which has lots of stuff in it.


#. Import something from Python's "standard library": ``randint`` from ``random``

#. Make a new file ``my_module.py``, define a variable ``MYVERSION`` in there, then
   import it in this ``game.py`` file.

#. When done, delete ``my_module.py``.


A Challenging Note
==================

Packages and libaries are interchangeable. Most Python people use "package"
to mean the thing you download and "libary" as the thing you use. It's
inconsistent.

A "module" is roughly the same as a file. Not always, but often enough.

Packages/libraries contain modules. Your code can also be organized into
modules. The module is where something like a function is defined.

Except, of course, when it isn't. One of the neat-but-confusing aspects
of libraries is that the top of the library can define stuff, to make
you not have to think about which module/file it is in.

Quiz
====

#. Give the name of a package and a function in the Python Standard
   Library?

#. What's the difference between importing the package itself, versus
   importing something in the package?

#. Does a module have to be in a library?

#. Does importing a module or library run anything?
