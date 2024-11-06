Changes
=======

0.10.0 (2024-11-DD)
-------------------

* Dropped official support for Python 3.8.

* The minimum supported versions of some dependencies have changed:

  * ``lxml``: ``4.4.1`` → ``4.5.2``
  * ``scikit-learn``: ``0.24.0`` → ``1.5.0``
  * ``scipy``: ``1.5.0`` → ``1.6.2``

* New dependencies have been added:

  * ``numpy`` ≥ ``1.19.5``
  * ``packaging`` ≥ ``14.0``
  * ``parsel`` ≥ ``1.1.0``
  * ``platformdirs`` ≥ ``3.2.0``

* The ``formasaurus.utils.dependencies_string()`` function is now deprecated.

* Added a new function, :func:`~formasaurus.build_submission`, to make
  Formasaurus :ref:`easier to use <usage>`.

* Added a built-in model, so that you can use Formasaurus right away without
  the need to first train a model on the built-in data.

* Changed the model serialization format, to minimize the chance of breakage
  due to new versions of dependencies.

  As a result, when specifying a model path, it is no longer the path to a
  single file, but the base path for multiple files. For example, if ``model``
  is specified as file path, 2 files are created, ``model-field.joblib`` and
  ``model-form.json``.

* When building a model, if a file path is not specified, the file path used by
  default is now guaranteed to be user-writable.

* Removed the need to specify the ``[with-deps]`` or ``[with_deps]`` extra when
  :ref:`installing <install>`.

* Improved the docs of :func:`~formasaurus.classifiers.extract_forms`.

0.9.0 (2024-06-19)
------------------

* Dropped official support for Python 3.7 and lower, and added official support
  for Python 3.8 and higher.

* Added support for the latest versions of all dependencies, and upgraded
  minimum supported versions of dependencies as follows:

  * ``docopt``: ``0.4.0``

  * ``requests``: ``1.0.0``

  * ``tldextract``: ``1.2.0``

  * ``with-deps`` extra dependencies:

    * ``joblib``: ``1.2.0``

    * ``lxml``: ``4.4.1``

    * ``lxml-html-clean``: ``0.1.0``

    * ``scikit-learn``: ``0.18.0`` → ``0.24.0``

    * ``scipy``: ``1.5.1``

    * ``sklearn-crfsuite``: ``0.3.1`` → ``0.5.1``

* https://github.com/scrapinghub/formasaurus is the new code repository,
  replacing https://github.com/TeamHG-Memex/Formasaurus.

* Updated the CI configuration and development tooling.

0.8.1 (2018-07-02)
------------------

* Support for scikit-learn < 0.18 is dropped;
* Formasaurus is no longer tested with Python 3.3;
* tests are fixed to account for upstream changes; Python 3.6 build is enabled.

0.8 (2016-05-24)
----------------

* more annotated data for captchas;
* ``formasaurus init`` command which trains & caches the model.

0.7.2 (2016-04-18)
------------------

* pip bug with ``pip install formasaurus[with-deps]`` is worked around;
  it should work now as ``pip install formasaurus[with_deps]``.

0.7.1 (2016-03-03)
------------------

* fixed API documentation at readthedocs.org

0.7 (2016-03-03)
----------------

* more annotated data;
* new ``form_classes`` and ``field_classes`` attributes of FormFieldClassifer;
* more robust web page encoding detection in ``formasaurus.utils.download``;
* bug fixes in annotation widgets;

0.6 (2016-01-27)
----------------

* ``fields=False`` argument is supported in ``formasaurus.extract_forms``,
  ``formasaurus.classify``, ``formasaurus.classify_proba`` functions and
  in related ``FormFieldClassifier`` methods. It allows to avoid predicting
  form field types if they are not needed.
* ``formasaurus.classifiers.instance()`` is renamed to
  ``formasaurus.classifiers.get_instance()``.
* Bias is no longer regularized for form type classifier.

0.5 (2015-12-19)
----------------

This is a major backwards-incompatible release.

* Formasaurus now can detect field types, not only form types;
* API is changed - check the updated documentation;
* there are more form types detected;
* evaluation setup is improved;
* annotation UI is rewritten using IPython widgets;
* more training data is added.

0.2 (2015-08-10)
----------------

* Python 3 support;
* fixed model auto-creation.

0.1 (2015-07-09)
----------------

Initial release.
