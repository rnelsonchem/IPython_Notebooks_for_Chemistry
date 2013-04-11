Introduction
============

These are a series of IPython Notebooks for exploring complex mathematical
concepts in chemistry. The notebooks are organized in folders according to
their area of application.

The Python script 'run_notebook.py' simply starts the notebook from folder
that it is located. This alleviates the need to understand the command line
instructions needed navigate to a particular folder and start the IPython
notebook. Just drop a copy of this script into the desired folder and run it
with Python. The method to run the script will be a little different depending
on your operating system and installation method. (If double-clicking the icon
doesn't work.  Try right-clicking on the icon. There may be an option to "Run
with..." where you can choose the Python interpreter.)

Installation
============

These Notebooks don't require any installation, *per se*. However, in order to
run them, you will need a minimal install of the newest releases of Python_ 2,
Numpy_, Matplotlib_, Scipy_, and IPython_ with all their associated
dependencies. This can be quite time consuming, but installation instructions
and binary installers for each package can be found from their respective
websites.

.. _Python: http://www.python.org/
.. _Numpy: http://www.numpy.org/
.. _Matplotlib: http://matplotlib.org/
.. _Scipy: http://www.scipy.org/
.. _IPython: http://ipython.org/

By far, the easiest way to install the necessary packages is to use one of the
prepackaged options for your operating system, such as `Python(x,y)`_
(Windows), `Enthought Python Distribution`_ (all OSes), Canopy_ (all OSes,
this is also from Enthought and is effectively the next-gen EPD, use this
first if possible), or `Anaconda`_ (all OS, broken uninstaller for Windows as
of v1.2.1).

.. _Python(x,y): http://code.google.com/p/pythonxy/
.. _Enthought Python Distribution: https://www.enthought.com/products/epd/
.. _Canopy: https://www.enthought.com/products/canopy/
.. _Anaconda: http://continuum.io/downloads.html

Some specific installation notes are provided here for reference.

EPD
---

The Enthought Python Distribution (EPD) has a very convenient package
management system, *enpkg*, which allows you to update packages with a few
simple commands. The only gotcha is that you must use the *sudo* command when
executing these commands on on a Mac/Linux.

https://support.enthought.com/entries/22415022-Using-enpkg-to-update-EPD-packages

Other Useful Installation Info 
------------------------------

http://fperez.org/py4science/starter_kit.html

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
    
