Coverage
########

..  include::   /references.inc

There is am old saying among programmers that goes like this:

    If you have not tested it, it does not work!

Applied to your code, every line of your program should be exercised during a test. The Coverage_ tool is designed to check your project to see if you are testing every line of code.

Installing Coverage
*******************

Installing is simple:

Add this line to the requirements.txt file::

..  code-block:: text

    coverage==4.0.3

Then run this command:

..  code-block:: bash

    $ pip install -r requirements.txt

We will integrate testing of the code using Tox_.

