twisted/python-info-action
==========================

Many CI configurations are setup to report various information about the environment they are running in.
This is usually done ad hoc resulting in lots of unnecessarily repeated code that often is missing relevant information.
This GitHub Action dumps various information relevant to the Python environment.


Warning
-------

This action is designed specifically to log environmental data.  Environment variables can often contain secrets which you may not want exposed.  The `github` context contains an authentication token.  In general, if you use GitHub's secrets feature then they will be masked in the build log.  The file output option will not have any redaction. Notes are included below about details.


Usage
-----

The point of providing this feature as a GitHub Action is that it can be easily added to your CI configuration with as little as a single line.

.. code-block:: yaml

    - uses: twisted/python-info-action@v1

If you need to specify a Python executable to use instead of what would be found by searching the path, you can pass it via ``python-path``.
This will be processed using bash so wildcards can be used.
One common use for this would be to create a tox environment using ``--notest``, use this action with ``python-path: .tox/the_env/*/python``, then actually run the tox environment after.

.. code-block:: yaml

    - uses: twisted/python-info-action@v1
      with:
        python-path: env/*/python

If you are not using GitHub's secrets feature, or otherwise want to mask environment variables for this action, you can just explicitly overwrite them.

.. code-block:: yaml

    - uses: twisted/python-info-action@v1
      env:
        A_SECRET: '<redacted>'

If you want the output stored to a file you can pass ``output-path``.  Remember that secrets will not generally be masked from this output.  Specifically note that the GitHub token will be present regardless.  For more explanation see |token_discussion|_.

.. code-block:: yaml

    - uses: twisted/python-info-action@v1
      with:
        output-path: environment.log

GitHub provides |uses_documentation|_.

.. |uses_documentation| replace:: more documentation for ``uses``
.. _uses_documentation: https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstepsuses
.. |token_discussion| replace:: a discussion about the token
.. _token_discussion: https://github.com/twisted/python-info-action/pull/11#discussion_r598122839

Compatibility
-------------

Basic tests are run against various Python versions and operating systems.

- Operating System
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

    sys.version              : 3.9.2 (default, Feb 19 2021, 19:41:08)
    [GCC 9.3.0]
    sys.prefix               : /opt/hostedtoolcache/Python/3.9.2/x64
    sys.exec_prefix          : /opt/hostedtoolcache/Python/3.9.2/x64
    sys.executable           : /opt/hostedtoolcache/Python/3.9.2/x64/bin/python
    struct.calcsize("P") * 8 : 64

    Environment Variables
    =====================

    'ACTION_FILE_PATH'                    : 'output_pre.log'
    'AGENT_TOOLSDIRECTORY'                : '/opt/hostedtoolcache'
    'ANDROID_HOME'                        : '/usr/local/lib/android/sdk'
    'ANDROID_NDK_HOME'                    : '/usr/local/lib/android/sdk/ndk-bundle'
    'ANDROID_NDK_LATEST_HOME'             : '/usr/local/lib/android/sdk/ndk/22.0.7026061'
    <snip>
    'SWIFT_PATH'                          : '/usr/share/swift/usr/bin'
    'USER'                                : 'runner'
    'VCPKG_INSTALLATION_ROOT'             : '/usr/local/share/vcpkg'
    '_'                                   : '/opt/hostedtoolcache/Python/3.9.2/x64/bin/python'
    'pythonLocation'                      : '/opt/hostedtoolcache/Python/3.9.2/x64'

    Installed Packages
    ==================

    pip==21.0.1
    setuptools==49.2.1

    Workflow Details
    ================


    Steps
    -----

    {}

    GitHub
    ------

    {
        "token": "***",
        "job": "ci",
        "ref": "refs/tags/v1",
        "sha": "49042d6852bce250821e1e91d8cea9e7d4dd5f81",
        "repository": "twisted/python-info-action",
        <snip>
        "action_repository": "",
        "action_ref": "",
        "path": "/home/runner/work/_temp/_runner_file_commands/add_path_4e829b24-d946-4a3b-9ffa-11f3ec54893c",
        "env": "/home/runner/work/_temp/_runner_file_commands/set_env_4e829b24-d946-4a3b-9ffa-11f3ec54893c",
        "action_path": "/home/runner/work/python-info-action/python-info-action/./"
    }

    Matrix
    ------

    {
        "os": {
            "name": "Linux",
            "runs-on": "ubuntu-latest"
        },
        "python": {
            "name": "CPython 3.9",
            "action": 3.9
        }
    }

    Runner
    ------

    {
        "os": "Linux",
        "tool_cache": "/opt/hostedtoolcache",
        "temp": "/home/runner/work/_temp",
        "workspace": "/home/runner/work/python-info-action"
    }

    Strategy
    --------

    {
        "fail-fast": false,
        "job-index": 5,
        "job-total": 27,
        "max-parallel": 27
    }

    Job
    ---

    {
        "status": "success"
    }


Support
-------

If you need help with usage, find an issue, or have some information you think would be appropriate for lots of CI runs to report...
Please `file an issue <https://github.com/twisted/python-info-action/issues/new>`_.
