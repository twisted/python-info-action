twisted/python-info-action
==========================

Many CI configurations are setup to report various information about the environment they are running in.
This is usually done ad hoc resulting in lots of unnecessarily repeated code that often is missing relevant information.
This GitHub Action dumps various information relevant to the Python environment.


Usage
-----

The point of providing this feature as a GitHub Action is that it can be easily added to your CI configuration with as little as a single line.

.. code-block:: yaml

    - uses: twisted/python-info-action@v1.0.1

If you need to specify a Python executable to use instead of what would be found by searching the path, you can pass it via ``python-path``.
This will be processed using bash so wildcards can be used.
One common use for this would be to create a tox environment using ``--notest``, use this action with ``python-path: .tox/the_env/*/python``, then actually run the tox environment after.

.. code-block:: yaml

    - uses: twisted/python-info-action@v1.2
      with:
        python-path: env/*/python


If you want the output stored to a file you can pass ``output-path``.

.. code-block:: yaml

    - uses: twisted/python-info-action@v1.0.1
      with:
        output-path: environment.log

GitHub provides |uses_documentation|_.

.. |uses_documentation| replace:: more documentation for ``uses``
.. _uses_documentation: https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstepsuses


Compatibility
-------------

Basic tests are run against various Python versions and operating systems.

- Operating
  - Linux
  - macOS
  - Windows
- Python
  - CPython 2.7, 3.5, 3.6, 3.7, 3.8, and 3.9
  - PyPy 2 and 3


Sample Output
-------------

.. code-block::

    Python Details
    ==============

    sys.version              : 3.9.0 (default, Oct 28 2020, 12:34:23)
    [GCC 9.3.0]
    sys.prefix               : /opt/hostedtoolcache/Python/3.9.0/x64
    sys.exec_prefix          : /opt/hostedtoolcache/Python/3.9.0/x64
    sys.executable           : /opt/hostedtoolcache/Python/3.9.0/x64/bin/python
    struct.calcsize("P") * 8 : 64

    Environment Variables
    =====================

    'ACTION_FILE_PATH'                  : 'output_pre.log'
    'AGENT_TOOLSDIRECTORY'              : '/opt/hostedtoolcache'
    ...
    'USER'                              : 'runner'
    'VCPKG_INSTALLATION_ROOT'           : '/usr/local/share/vcpkg'
    '_'                                 : '/opt/hostedtoolcache/Python/3.9.0/x64/bin/python'
    'pythonLocation'                    : '/opt/hostedtoolcache/Python/3.9.0/x64'

    Installed Packages
    ==================

    pip==20.2.4
    setuptools==49.2.1

Support
-------

If you need help with usage, find an issue, or have some information you think would be appropriate for lots of CI runs to report...
Please `file an issue <https://github.com/twisted/python-info-action/issues/new>`_.
