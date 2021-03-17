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
    'ANDROID_HOME'                      : '/usr/local/lib/android/sdk'
    'ANDROID_SDK_ROOT'                  : '/usr/local/lib/android/sdk'
    'ANT_HOME'                          : '/usr/share/ant'
    'AZURE_EXTENSION_DIR'               : '/opt/az/azcliextensions'
    'CHROMEWEBDRIVER'                   : '/usr/local/share/chrome_driver'
    'CHROME_BIN'                        : '/usr/bin/google-chrome'
    'CI'                                : 'true'
    'CONDA'                             : '/usr/share/miniconda'
    'DEBIAN_FRONTEND'                   : 'noninteractive'
    'DEPLOYMENT_BASEPATH'               : '/opt/runner'
    'DOTNET_MULTILEVEL_LOOKUP'          : '"0"'
    'DOTNET_NOLOGO'                     : '"1"'
    'DOTNET_SKIP_FIRST_TIME_EXPERIENCE' : '"1"'
    'GECKOWEBDRIVER'                    : '/usr/local/share/gecko_driver'
    'GITHUB_ACTION'                     : 'self1'
    'GITHUB_ACTIONS'                    : 'true'
    'GITHUB_ACTION_PATH'                : '/home/runner/work/python-info-action/python-info-action/./'
    'GITHUB_ACTION_REF'                 : 'v2'
    'GITHUB_ACTION_REPOSITORY'          : 'actions/setup-python'
    'GITHUB_ACTOR'                      : 'altendky'
    'GITHUB_API_URL'                    : 'https://api.github.com'
    'GITHUB_BASE_REF'                   : 'main'
    'GITHUB_ENV'                        : '/home/runner/work/_temp/_runner_file_commands/set_env_a54c197b-071c-42f2-bbf4-09281fe3a938'
    'GITHUB_EVENT_NAME'                 : 'pull_request'
    'GITHUB_EVENT_PATH'                 : '/home/runner/work/_temp/_github_workflow/event.json'
    'GITHUB_GRAPHQL_URL'                : 'https://api.github.com/graphql'
    'GITHUB_HEAD_REF'                   : 'initial'
    'GITHUB_JOB'                        : 'ci'
    'GITHUB_PATH'                       : '/home/runner/work/_temp/_runner_file_commands/add_path_a54c197b-071c-42f2-bbf4-09281fe3a938'
    'GITHUB_REF'                        : 'refs/pull/1/merge'
    'GITHUB_REPOSITORY'                 : 'twisted/python-info-action'
    'GITHUB_REPOSITORY_OWNER'           : 'twisted'
    'GITHUB_RETENTION_DAYS'             : '90'
    'GITHUB_RUN_ID'                     : '387884747'
    'GITHUB_RUN_NUMBER'                 : '19'
    'GITHUB_SERVER_URL'                 : 'https://github.com'
    'GITHUB_SHA'                        : '5a75a5db452f7e3e4fb2d5a60b74f3b226b4e1ae'
    'GITHUB_WORKFLOW'                   : 'CI'
    'GITHUB_WORKSPACE'                  : '/home/runner/work/python-info-action/python-info-action'
    'GOROOT'                            : '/opt/hostedtoolcache/go/1.14.12/x64'
    'GOROOT_1_14_X64'                   : '/opt/hostedtoolcache/go/1.14.12/x64'
    'GOROOT_1_15_X64'                   : '/opt/hostedtoolcache/go/1.15.5/x64'
    'GRADLE_HOME'                       : '/usr/share/gradle'
    'HOME'                              : '/home/runner'
    'HOMEBREW_CELLAR'                   : '"/home/linuxbrew/.linuxbrew/Cellar"'
    'HOMEBREW_PREFIX'                   : '"/home/linuxbrew/.linuxbrew"'
    'HOMEBREW_REPOSITORY'               : '"/home/linuxbrew/.linuxbrew/Homebrew"'
    'INVOCATION_ID'                     : 'be50e50f7ee7408a8ede602afbf313ec'
    'ImageOS'                           : 'ubuntu20'
    'ImageVersion'                      : '20201116.1'
    'JAVA_HOME'                         : '/usr/lib/jvm/adoptopenjdk-11-hotspot-amd64'
    'JAVA_HOME_11_X64'                  : '/usr/lib/jvm/adoptopenjdk-11-hotspot-amd64'
    'JAVA_HOME_8_X64'                   : '/usr/lib/jvm/adoptopenjdk-8-hotspot-amd64'
    'JOURNAL_STREAM'                    : '9:20579'
    'LANG'                              : 'C.UTF-8'
    'LD_LIBRARY_PATH'                   : '/opt/hostedtoolcache/Python/3.9.0/x64/lib'
    'LEIN_HOME'                         : '/usr/local/lib/lein'
    'LEIN_JAR'                          : '/usr/local/lib/lein/self-installs/leiningen-2.9.4-standalone.jar'
    'M2_HOME'                           : '/usr/share/apache-maven-3.6.3'
    'PATH'                              : '/opt/hostedtoolcache/Python/3.9.0/x64/bin:/opt/hostedtoolcache/Python/3.9.0/x64:/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:/opt/pipx_bin:/usr/share/rust/.cargo/bin:/home/runner/.config/composer/vendor/bin:/home/runner/.dotnet/tools:/snap/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
    'PERFLOG_LOCATION_SETTING'          : 'RUNNER_PERFLOG'
    'PIPX_BIN_DIR'                      : '"/opt/pipx_bin"'
    'PIPX_HOME'                         : '"/opt/pipx"'
    'POWERSHELL_DISTRIBUTION_CHANNEL'   : 'GitHub-Actions-ubuntu20'
    'PWD'                               : '/home/runner/work/python-info-action/python-info-action'
    'RUNNER_OS'                         : 'Linux'
    'RUNNER_PERFLOG'                    : '/home/runner/perflog'
    'RUNNER_TEMP'                       : '/home/runner/work/_temp'
    'RUNNER_TOOL_CACHE'                 : '/opt/hostedtoolcache'
    'RUNNER_TRACKING_ID'                : 'github_02a261ae-7169-4a49-a99b-3dc10b5ffe62'
    'RUNNER_USER'                       : 'runner'
    'RUNNER_WORKSPACE'                  : '/home/runner/work/python-info-action'
    'SELENIUM_JAR_PATH'                 : '/usr/share/java/selenium-server-standalone.jar'
    'SHLVL'                             : '1'
    'SWIFT_PATH'                        : '/usr/share/swift/usr/bin'
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
