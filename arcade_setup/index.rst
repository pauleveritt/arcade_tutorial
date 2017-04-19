============
Arcade Setup
============

Nothing is more frustrating than trying to start, only to find you aren't
setup correctly. Let's write a tiny program to ensure that:

- Arcade is installed correctly, and...

- For those using PyCharm, we can run our small Python program

.. youtube:: d3NxblctHJI

Steps
=====

#. Make sure you have the ``arcade_tutorial`` project open in PyCharm.

#. In the PyCharm menu, choose ``File -> New -> Python File``, then name
   file ``game.py``.

#. In the new file, enter the following:

   .. literalinclude:: game.py
        :language: python
        :linenos:

#. Right-click in the middle of the file and choose ``Run 'game'``.

#. A panel should appear at the bottom with an error message -- we
   haven't installed ``arcade`` yet into this virtual environment!

#. Click on the red-squigly line for ``arcade`` on line one, then click on
   the red light bulb that pops up.

#. Choose the ``Install package arcade`` menu item.

#. Once installed, click the green play button to re-run our program.

#. You now see, in the ``Run`` window, the version number.

What's Going On
===============

In this step we ran a Python program. Cool! We used the Python that we
setup as the virtual environment for this project, then created a new file
called ``game.py`` and told that Python to run the file.

Actually, we told *PyCharm* to tell Python to run it, then PyCharm helped
along the way. For example, the output went to a nice output window.

But we had a problem the first time. Our program wants to use some
software that isn't in Python itself. The software, called *Arcade*,
has to be installed. PyCharm offered to install this Python *package*
into this project's virtual environment. We could then *import* the code
from Arcade, into the file we are working on.

Finally, we did our one piece of work for this "game": we grabbed a
*variable* from the Arcade package (what version of Arcade we have
installed) and used the print *function* to send that variable's value
to the output.

Terms Used
==========

- *import*. A Python statement to get the code from another location
  and bring it into the file you are working in.

- *Function*.

- variable

