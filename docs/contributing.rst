Contributing
============

Development
-----------

* Source code: https://github.com/scrapinghub/Formasaurus
* Issue tracker: https://github.com/scrapinghub/Formasaurus/issues

Feel free to submit ideas, bugs reports and pull requests.

In order to run tests install tox_, then type

::

    tox

from the source checkout.

.. _tox: http://tox.testrun.org


The easiest way to improve classification quality is to add more training
examples. Use "Add New Pages" and "Annotate" IPython notebooks for that.

If you want to improve Formasaurus ML models check :ref:`how-it-works` section.

Generating the built-in model
-----------------------------

Every time we improve the training data, we should re-train the built-in model:

.. code-block:: python

    python3 -m venv venv
    . venv/bin/activate
    pip install .[with-deps]
    python3 utils/build.py

We also need to update it if it becomes incompatible with a newer version of
some dependencies, as well as updating the minimum versions of dependencies in
setup.py and tox.ini[min] accordingly.

Authors
-------

* Mikhail Korobov <kmike84@gmail.com>

License
-------

License is MIT.
