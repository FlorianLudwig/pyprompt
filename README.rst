pyprompt
========

bash prompt written in python.

.. image:: https://raw.githubusercontent.com/FlorianLudwig/pyprompt/master/docs/screenshot.png

The prompt is using a two line layout:

* info-line (username, hostname and current directory) and input are on seperates line
* full path is dispalyed
* if you are into mouse usage from time to time, the path is seperated from the hostname by a space so double clicking the path selects only the path (at least in `gnome-terminal`)
* the background color fills the terminal size so commands have a nice seperator between them.  Also the backgroun color does indicate if the last command had a non zero return code

usage
-----

.. code-block:: bash

    pip install pyprompt
    # set PS1 environment variable (for example in your .bashrc)
    PS1="\$(pyprompt \$?)"
