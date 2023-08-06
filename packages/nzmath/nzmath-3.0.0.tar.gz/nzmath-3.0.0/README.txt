NZMATH 3.0.0 (Python 3 calculator on number theory)
===================================================

Introduction
------------

NZMATH is a Python based number theory oriented calculation system.
Its development started at Nakamula laboratory, Tokyo Metropolitan
University.  Today it is developed at SourceForge.net .

This version 3.0.0 is based on Python 3, while former versions are all
based on Python 2.  Most features are equal to those of version 1.2.0.
The API can still be changed with versions.

Installation
------------

To install NZMATH on your computer, you must have Python 3.8 or later.
If you don't have a copy of Python, please install it first.
Python is available from https://www.python.org/ .

The next step is to expand the NZMATH-3.0.0.tar.gz.  The way to do it
depends on your operating system.  On the systems with recent GNU tar,
you can do it with a single command::

 % tar xf NZMATH-3.0.0.tar.gz

where, % is the command line prompt.  Or with standard tar, you can do
it as::

 % gzip -cd NZMATH-3.0.0.tar.gz | tar xf -

Then, you have a child directory named NZMATH-3.0.0.

The third step is the last step, to install NZMATH to the standard
python path.  Usually, this means to write files to somewhere under
/usr/lib or /usr/local/lib, and thus you have to have appropriate
write permission.  Typically, do as the following::

 % cd NZMATH-3.0.0
 % su
 # python setup.py install

Usage
-----

NZMATH is provided as a Python library package named 'nzmath', so
please use it as a usual package.  For more information please refer
Tutorial_.

.. _Tutorial: tutorial.html

Feedback
--------

Your feedbacks are always welcomed.  Please consider to join the
mailing list nzmath-user@lists.sourceforge.net .  You can join the list
by visiting the web page
https://lists.sourceforge.net/lists/listinfo/nzmath-user .

Copyright
---------

NZMATH is distributed under the BSD license.  Please read LICENSE.txt_
in the distribution tar ball for detail.

.. _LICENSE.txt: LICENSE.txt


AddressObject
