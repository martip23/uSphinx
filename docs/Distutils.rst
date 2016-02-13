Distutils
#########

Almost all major Python tools are distributed as part of the Pypi_ project. You
need to register as a developer to be able to host your project on this
service, but this is free and easy to do.

Once you are properly registered, all you need to do is ad a few basic files to
your project.

setup.py
********

Here is a basic `setup.py` file from this project:

..  literalinclude::    ../setup.py

Register Project
****************

With a suitable `setup.py` file, we can register the project using this command:

..  code-block:: bash

    $ python setup.py register


Upload Project
**************

When you have a new version of the project redy, you can upload it to Pypi_ as follows:

..  code-block:: bash

    $ python setup.py upload.

