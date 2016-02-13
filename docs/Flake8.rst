Flake8
######

..  include::   /references.inc

The Flake8_ tool checks your python code to make sure it follows accepted style conventions. This is a good way to make sure your code is "presentable" and not littered with inconsistent indentiong and other ills.

Installing Flake8
*****************

Installing is simple:

Add this line to the requirements.txt file::

..  code-block:: text

    flake8==2.5.4

Then run this command:

..  code-block:: bash

    $ pip install -r requirements.txt

We will integrate testing of the code using Tox_.

