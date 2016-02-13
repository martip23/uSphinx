Continuous Integration with TravisCI
####################################

In today's fast paced world, you need to be sure your application is ready for those users out there you hope will use your product. If you do all of your development on one platform, you may be surprised to find it just does not work on other platforms at all.

I deal with this situation as a teacher all the time. Our school uses mostly Windows machines in the labs, but students show up for classes with a wide variety of systems. I routinely have a mix of WIndows and Mac versions, and even the ocassional Linux machine. All of these students want to use their personal machines for class work, but the schools setup is the only "official" system we support. I have not based my classes on that, and do try to help students get set up on their current machine. For me, that makes my life a bit more complex, since students will be using several different tools in a given class, not one "official tool. For that reason, I usually have a setup the supports the "big three" WIndows, Mac, and Linux. Currently, I carry a Macbook Pro with the latest version of oS-X, A WIndows Surface running WIndows 10, and I run a virtual machine onmy Mac with Ubunto LInux installed. 

So, if your appliation is going to work anywhere, you need to be able to test that application on several different platforms. Fortunately, there are several services available for free (for open source projects) or at least inexpensively, to let you run you application on a different system configuration, just to make sure everything id ready for production.

I use TravisCI_ as my first step in testing on rmeote systems. This service, like others, ties to GitHUb in a way that runs tests on your code every time you push changes to GitHub. Once you have your project on GitHub_, you activate the TravisCI_ hook that will automaticaly pull your changes to their server where they will run your testing code and report the results.

The most common way you check these results is through a "badge" which is a simple graphic image saying something like "build:passing". If you place a link to thei badge on the README file in your project's root diectory, it will display for all folks visiting your GihHub project. Having a set of good badge images is becoming simething of a status symbol for projects, these days!

Setting Up
**********

You need ot sign up for an account for TravisCI, and you can do this using your GutHub_ credentials. Once that is done, all you need to do to start testing on TravisCI is to turn on the repository link on the TravisCI control panel, and add one file to the root of your project. 

TravisCI Configuration File
===========================

Here is an example control file. It must be named `.travis.yml` and be placed at the root level of your repository.

..  literalinclude::    ../.travis.yml
    :linenos:
    :language: yaml



