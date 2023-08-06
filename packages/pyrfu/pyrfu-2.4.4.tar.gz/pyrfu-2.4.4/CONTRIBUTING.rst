Contributing to pyrfu
=====================
.. start-marker-style-do-not-remove

The following is a set of guidelines for contributing to ``pyrfu`` and its packages, which are hosted on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

Introduction
------------
This guide defines the conventions for writing Python code for ``pyrfu``.
The main ideas are:

-  ensuring a consistent code style
-  promote good practices for testing
-  maintaining a good level of readability and maintainability
-  to keep it simple


Python version
--------------
Prefer if possible Python>=3.8 since there are major dependencies that do not support
older python versions.


Coding style
------------
The pyrfu package uses the `Black code style <https://black.readthedocs
.io/en/stable/the_black_code_style/current_style.html>`__ .

Use Linters
------------
Linters are tools for static code quality checker. For instance, you can
use the following tools to test conformity with the common pythonic
standards:

- `pylint <http://pylint.pycqa.org/en/latest/user_guide/output.html>`__ is one of the oldest linters and tracks various problems such as good practice violation, coding standard violation, or programming issues. Pylint may be seen as slow, too verbose and complex to configure to get it working properly. You can run a complete static analysis with the following command:

.. code:: python

    pylint pyrfu --rcfile=setup.cfg

All these linters can be simply installed with pip. Further details
on the functionnalities can be found
`here <http://books.agiliq.com/projects/essential-python-tools/en/latest/linters.html>`__
or `there <https://realpython.com/python-code-quality/>`__.
Also, a lot of features can also be provided natively or by installing
plugins with your IDE (PyCharm, Spyder, Eclipse, etc.).

To be accepted to ``pyrfu`` every new code as to get a pylint score of 10/10.

Documentation
-------------
Documentation of all the files must be done in-line using Sphinx_.
The doxtring as to follow the numpydoc_ style

.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html

