Testing with Tox
################

..  include::   /references.inc

Tox_ is a tool that automates testing of Python applications in a number of environments. Tox_ sets up a virtualenv_ for multiple versions of Python and runs tests to make sure the application performs correctly in each environment. Tox_ helps streamline running tests on a `Continuous Integratin Service` like TravisCI_.

Installing Tox
**************

To get started, add this line to the `rewuirements.txt` file:

..  code-block:: text
    
    tox==2.3.1

Run Pip_ as usual to complete the installation:

..  code-block:: text

    $ pip install -r requirements.txt

