Introduction
============

These are a series of interactive worksheets for exploring complex
mathematical concepts in chemistry. These worksheets must be run using
the new web-based notebook_ interface to IPython_, which is an advanced,
interactive interpreter for the Python_ programming language. IPython was
specifically designed for interactive, scientific data analysis and
simulation, so it is an ideal tool for exploring mathematical concepts related
to chemistry. In it's original incarnation, IPython was designed to be run
from inside a terminal or command prompt window; however, the newest releases
have a web-based notebook like interface that allows not only for interactive
code generation but also textual markup that can be used to explain the
code workings.

The main point of these notebooks is to teach mathematical concepts related to
chemistry. With that in mind, large portions of the underlying Python code
have been abstracted from the main worksheet. Some small amount of code
has been left in to allow students to interactively modify variable
values to explore the changes in simulated data. 

A secondary goal of these notebooks is to teach Python programming as a
powerful method of data analysis, so the abstracted code is contained in
Python program files (ending in *\.py*) contained in the individual notebook
folders. These files are simple text files that can be read with any text
editor. Students that are interested in learning more about how the data is
actually manipulated are encouraged to explore these files on their own. A
number of Python programming tutorials are available on the web; however, many
are geared towards computer scientists and programmers. The `Scientific Python
Lecture Notes`_ are a continually-evolving tutorial geared toward scientists
interested in learning Python and some third-party libraries in the context of
scientific work. In addition, several interactive Python tutorials are
contained in this download; however, these will not be as comprehensive as
other tutorials on the web.

These notebooks are organized into folders according to their area of
application. The Python script 'run_notebook.py' starts the IPython notebook
server from the folder that it is located.  This alleviates the need to
understand the command line instructions necessary to navigate to a particular
folder and start the IPython notebook. Just drop a copy of this script into
the desired folder and run it with Python. The method to run the script will
be a little different depending on your operating system and installation
method. (If double-clicking the icon doesn't work.  Try right-clicking on the
icon. There may be an option to "Run with..." where you can choose the Python
interpreter.)

Installation
============

These notebooks don't require any installation, *per se*. However, in order to
run them, you will need a minimal install of the newest releases of Python_ 2,
Numpy_, Matplotlib_, Scipy_, and IPython_ with all their associated
dependencies. This installation method can be quite time consuming, but
installation instructions and binary installers for each package can be found
from their respective websites.

By far, the easiest way to install the necessary packages is to use one of the
prepackaged options for your operating system, such as `Python(x,y)`_
(Windows), Canopy_ (all OSes, this is also from Enthought and is effectively
the next-gen EPD, use this first if possible), `Enthought Python
Distribution`_ (EPD, all OSes), or `Anaconda`_ (all OS, broken uninstaller for
Windows as of v1.2.1).

Some specific installation notes are provided here for reference.

EPD
---

The Enthought Python Distribution (EPD) has a very convenient package
management system, *enpkg*, which allows you to update packages with a few
simple commands. The only gotcha is that you must use *sudo* when executing
these commands on on a Mac/Linux.

Jonathan March at Enthought has a nice article_ in the `Enthought Knowledge
Base`_ that describes how to update packages using this function.

Other Useful Installation Info 
------------------------------

Fernando Perez, the original author of IPython, has a short webpage_ devoted
to Python for scientific applications, which contains a variety of
installation notes.

Potential Pitfalls
==================

This is a collection of pitfalls that have been encountered in installing and
running these notebooks.

* Older version of IE and very old versions of Firefox are not supported by
  IPython. You should use the newest versions of Firefox or Chrome for the
  best results.

* These notebooks can be downloaded from GitHub as a zip package. The zip
  package must be explicitly extracted for the IPython notebook to function
  properly.

* Antivirus software may try to block the IPython notebook software. If you
  run a notebook cell and it hangs for a very long time, then you may be
  having these issues. As a test, open a new notebook and type 'print "hello"'
  in the first cell. Try running the cell with Shift-Enter. If the notebook
  hangs at this point, then your antivirus software may be to blame.

    - Sophos on Windows: (You must be an administrator on your computer. If
      not, talk to your IT people.) Click the Windows icon in the lower left.
      Type 'services.msc' in the search bar (or in 'Run...' on Windows XP),
      and run this process. Stop 'Sophos Web Control Service' and 'Sophos Web
      Intelligence Service'. Restart the IPython Notebook and you should be
      all set.


.. _Python: http://www.python.org/
.. _Numpy: http://www.numpy.org/
.. _Matplotlib: http://matplotlib.org/
.. _Scipy: http://www.scipy.org/
.. _IPython: http://ipython.org/
.. _Python(x,y): http://code.google.com/p/pythonxy/
.. _Enthought Python Distribution: https://www.enthought.com/products/epd/
.. _Canopy: https://www.enthought.com/products/canopy/
.. _Anaconda: http://continuum.io/downloads.html
.. _notebook: http://ipython.org/notebook.html
.. _webpage: http://fperez.org/py4science/starter_kit.html
.. _article: https://support.enthought.com/entries/22415022-Using-enpkg-to-update-EPD-packages
.. _Enthought Knowledge Base: https://support.enthought.com/forums 
.. _Scientific Python Lecture Notes: http://scipy-lectures.github.io/ 
