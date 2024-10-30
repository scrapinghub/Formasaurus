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

Generating built-in models
--------------------------

Every time we improve the training data, we should re-train the built-in model:

.. code-block:: sh

    pip install .
    python utils/build.py

Authors
-------

* Mikhail Korobov <kmike84@gmail.com>

License
-------

License is MIT.
