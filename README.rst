pyprompt
========

bash prompt written in python.

.. image:: https://raw.githubusercontent.com/FlorianLudwig/pyprompt/master/docs/screenshot.png

The prompt is using a two line layout:

* info-line (username, hostname and current directory) and input are on separate lines
* full path is displayed
* the info line uses a background color to create a visual separator between the commands you run.  The background color doubles as indicator if the last command had a non zero return code
* if you are into mouse usage from time to time, the path is separated from the hostname by a space so double clicking the path selects only the path (at least in `gnome-terminal`)

usage
-----

.. code-block:: bash

    pip install pyprompt
    # set PS1 environment variable (for example in your .bashrc)
    PS1="\$(pyprompt \$?)"

