Git Flow Development Scheme
###########################

..  include /references.inc

..  _`Semantic Versions <http://semver.org/>`_

The Git_ community has created a variety of tools to help manage projects more
efficiently. For my development of uSphinx_, I am going to use `git-flow` to
track the development.

Project Startup
***************

Starting a new Python project is a common thing I do, so I have a template for
doing this:

..  code-block:: bash

    $ cd _projects
    $ mkdir uSphinx
    $ venv
    $ git flow init -d
    $ cp ~/lib/.gitignore .

The first command is a bash alias I create that looks like this:

..  code-block:: bash

    alias workon='source _venv/bin/activate
    alias venv=`virtualenv _venv && workon'

I like to use underscores as the lead character in directory names to make does
directories appear at the top of directory lists in tools like WIndows
Explorers or Mac FInder. YMMV.

Project Development
*******************

In my notes, I want to be able to show code written at each stage of
development. Since I use Git_ to manage my code, I will be using version
numbering to track major changes to the code base.

The numbering scheme I will use is common enough that it should be easy to
follow:

    * v<release><feature><hotfix>

Some authors use this scheme for identifying the version numbering:

    * v<major><minor><patch>

The last digit is reserved for bug-fixes made after the parent numbering has
been established.

Tagging Versions
****************

Git-FLow_ creates version tags when a release if made. 


Using Git-Flow, we work on new features as we develop code. Each feature is
started using this command:

..  code-block:: bash

    $ git flow feature start 
