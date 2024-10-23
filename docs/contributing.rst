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

Every time we improve the training data or a new minor version of scikit-learn
is released, we should re-train the built-in models:

#.  Update ``utils/SKL_VERSIONS.txt`` with all versions of scikit-learn for
    which a model should be pre-built. It should contain the latest patch
    version for every supported minor version, separated by a space, e.g.

    .. code-block:: none

        1.4.2 1.5.2

#.  Run the following Bash script to build a model for each scikit-learn
    version:

    .. code-block:: sh

        bash utils/build.sh

Authors
-------

* Mikhail Korobov <kmike84@gmail.com>

License
-------

License is MIT.
