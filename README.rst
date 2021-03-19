twisted/python-info-action
==========================

Many CI configurations are setup to report various information about the environment they are running in.
This is usually done ad hoc resulting in lots of unnecessarily repeated code that often is missing relevant information.
This GitHub Action dumps various information relevant to the Python environment.


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


If you want the output stored to a file you can pass ``output-path``.

.. code-block:: yaml

    - uses: twisted/python-info-action@v1
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
    'ANDROID_NDK_ROOT'                    : '/usr/local/lib/android/sdk/ndk-bundle'
    'ANDROID_SDK_ROOT'                    : '/usr/local/lib/android/sdk'
    'ANT_HOME'                            : '/usr/share/ant'
    'AZURE_EXTENSION_DIR'                 : '/opt/az/azcliextensions'
    'BOOTSTRAP_HASKELL_NONINTERACTIVE'    : '1'
    'CHROMEWEBDRIVER'                     : '/usr/local/share/chrome_driver'
    'CHROME_BIN'                          : '/usr/bin/google-chrome'
    'CI'                                  : 'true'
    'CONDA'                               : '/usr/share/miniconda'
    'DEBIAN_FRONTEND'                     : 'noninteractive'
    'DEPLOYMENT_BASEPATH'                 : '/opt/runner'
    'DOTNET_MULTILEVEL_LOOKUP'            : '0'
    'DOTNET_NOLOGO'                       : '1'
    'DOTNET_SKIP_FIRST_TIME_EXPERIENCE'   : '1'
    'GECKOWEBDRIVER'                      : '/usr/local/share/gecko_driver'
    'GITHUB_ACTION'                       : 'self1'
    'GITHUB_ACTIONS'                      : 'true'
    'GITHUB_ACTION_PATH'                  : '/home/runner/work/python-info-action/python-info-action/./'
    'GITHUB_ACTION_REF'                   : ''
    'GITHUB_ACTION_REPOSITORY'            : ''
    'GITHUB_ACTOR'                        : 'altendky'
    'GITHUB_API_URL'                      : 'https://api.github.com'
    'GITHUB_BASE_REF'                     : ''
    'GITHUB_ENV'                          : '/home/runner/work/_temp/_runner_file_commands/set_env_827030a9-258d-4950-995f-a89a2497f7a2'
    'GITHUB_EVENT_NAME'                   : 'push'
    'GITHUB_EVENT_PATH'                   : '/home/runner/work/_temp/_github_workflow/event.json'
    'GITHUB_GRAPHQL_URL'                  : 'https://api.github.com/graphql'
    'GITHUB_HEAD_REF'                     : ''
    'GITHUB_JOB'                          : 'ci'
    'GITHUB_PATH'                         : '/home/runner/work/_temp/_runner_file_commands/add_path_827030a9-258d-4950-995f-a89a2497f7a2'
    'GITHUB_REF'                          : 'refs/tags/v1'
    'GITHUB_REPOSITORY'                   : 'twisted/python-info-action'
    'GITHUB_REPOSITORY_OWNER'             : 'twisted'
    'GITHUB_RETENTION_DAYS'               : '90'
    'GITHUB_RUN_ID'                       : '649833066'
    'GITHUB_RUN_NUMBER'                   : '177'
    'GITHUB_SERVER_URL'                   : 'https://github.com'
    'GITHUB_SHA'                          : '49042d6852bce250821e1e91d8cea9e7d4dd5f81'
    'GITHUB_WORKFLOW'                     : 'CI'
    'GITHUB_WORKSPACE'                    : '/home/runner/work/python-info-action/python-info-action'
    'GOROOT_1_14_X64'                     : '/opt/hostedtoolcache/go/1.14.15/x64'
    'GOROOT_1_15_X64'                     : '/opt/hostedtoolcache/go/1.15.8/x64'
    'GOROOT_1_16_X64'                     : '/opt/hostedtoolcache/go/1.16.0/x64'
    'GRAALVM_11_ROOT'                     : '/usr/local/graalvm/graalvm-ce-java11-21.0.0.2'
    'GRADLE_HOME'                         : '/usr/share/gradle'
    'HOME'                                : '/home/runner'
    'HOMEBREW_CELLAR'                     : '"/home/linuxbrew/.linuxbrew/Cellar"'
    'HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS' : '3650'
    'HOMEBREW_NO_AUTO_UPDATE'             : '1'
    'HOMEBREW_PREFIX'                     : '"/home/linuxbrew/.linuxbrew"'
    'HOMEBREW_REPOSITORY'                 : '"/home/linuxbrew/.linuxbrew/Homebrew"'
    'INVOCATION_ID'                       : 'b7e3f0962f764bb4821eb641eff332da'
    'ImageOS'                             : 'ubuntu20'
    'ImageVersion'                        : '20210302.0'
    'JAVA_HOME'                           : '/usr/lib/jvm/adoptopenjdk-11-hotspot-amd64'
    'JAVA_HOME_11_X64'                    : '/usr/lib/jvm/adoptopenjdk-11-hotspot-amd64'
    'JAVA_HOME_8_X64'                     : '/usr/lib/jvm/adoptopenjdk-8-hotspot-amd64'
    'JOURNAL_STREAM'                      : '9:19343'
    'LANG'                                : 'C.UTF-8'
    'LD_LIBRARY_PATH'                     : '/opt/hostedtoolcache/Python/3.9.2/x64/lib'
    'LEIN_HOME'                           : '/usr/local/lib/lein'
    'LEIN_JAR'                            : '/usr/local/lib/lein/self-installs/leiningen-2.9.5-standalone.jar'
    'PATH'                                : '/opt/hostedtoolcache/Python/3.9.2/x64/bin:/opt/hostedtoolcache/Python/3.9.2/x64:/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:/opt/pipx_bin:/usr/share/rust/.cargo/bin:/home/runner/.config/composer/vendor/bin:/usr/local/.ghcup/bin:/home/runner/.dotnet/tools:/snap/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
    'PERFLOG_LOCATION_SETTING'            : 'RUNNER_PERFLOG'
    'PIPX_BIN_DIR'                        : '/opt/pipx_bin'
    'PIPX_HOME'                           : '/opt/pipx'
    'POWERSHELL_DISTRIBUTION_CHANNEL'     : 'GitHub-Actions-ubuntu20'
    'PWD'                                 : '/home/runner/work/python-info-action/python-info-action'
    'RUNNER_OS'                           : 'Linux'
    'RUNNER_PERFLOG'                      : '/home/runner/perflog'
    'RUNNER_TEMP'                         : '/home/runner/work/_temp'
    'RUNNER_TOOL_CACHE'                   : '/opt/hostedtoolcache'
    'RUNNER_TRACKING_ID'                  : 'github_eb40fa08-b43b-4cc2-9f54-726413848d06'
    'RUNNER_USER'                         : 'runner'
    'RUNNER_WORKSPACE'                    : '/home/runner/work/python-info-action'
    'SELENIUM_JAR_PATH'                   : '/usr/share/java/selenium-server-standalone.jar'
    'SHLVL'                               : '1'
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
        "token": "v1.0c46741a32436f591105a1c12ee7000683bfb58e",
        "job": "ci",
        "ref": "refs/tags/v1",
        "sha": "49042d6852bce250821e1e91d8cea9e7d4dd5f81",
        "repository": "twisted/python-info-action",
        "repository_owner": "twisted",
        "repositoryUrl": "git://github.com/twisted/python-info-action.git",
        "run_id": "649833066",
        "run_number": "177",
        "retention_days": "90",
        "actor": "altendky",
        "workflow": "CI",
        "head_ref": "",
        "base_ref": "",
        "event_name": "push",
        "event": {
            "after": "49042d6852bce250821e1e91d8cea9e7d4dd5f81",
            "base_ref": "refs/heads/main",
            "before": "bd29f742850004f97c8f69ce9b092728246e3d0c",
            "commits": [
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "ea1b7e183b3bc20c0edbea69641d34ed08a47f27",
                    "message": "Add python_path as a parameter",
                    "timestamp": "2021-03-01T16:33:55-05:00",
                    "tree_id": "0c47451888979c3fd386840176be0f7234d4068d",
                    "url": "https://github.com/twisted/python-info-action/commit/ea1b7e183b3bc20c0edbea69641d34ed08a47f27"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "38060b4cd18f13caa433ad9a640a68b13ea42e1e",
                    "message": "it is python_path",
                    "timestamp": "2021-03-01T16:36:31-05:00",
                    "tree_id": "cf3a2ca9eed1c98b5c5b54d4efcd3613481ab112",
                    "url": "https://github.com/twisted/python-info-action/commit/38060b4cd18f13caa433ad9a640a68b13ea42e1e"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "noreply@github.com",
                        "name": "GitHub",
                        "username": "web-flow"
                    },
                    "distinct": false,
                    "id": "5151ff8557ac7300f444311aad07f82395bdbe59",
                    "message": "Update action.yml",
                    "timestamp": "2021-03-01T16:41:10-05:00",
                    "tree_id": "4a9551ed366e1cae2a3d9281928f91028d275d04",
                    "url": "https://github.com/twisted/python-info-action/commit/5151ff8557ac7300f444311aad07f82395bdbe59"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "4f96453cffc34ec5b23e6daef82323e1d7eedd65",
                    "message": "fix the prefix test",
                    "timestamp": "2021-03-01T16:48:54-05:00",
                    "tree_id": "9009992c316e8ba7451753d6fbfc7ff78110b467",
                    "url": "https://github.com/twisted/python-info-action/commit/4f96453cffc34ec5b23e6daef82323e1d7eedd65"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "50228b7fc4ecef6feefec9d2be84a59d44aa15bb",
                    "message": "use virtualenv to handle py2",
                    "timestamp": "2021-03-01T16:51:18-05:00",
                    "tree_id": "99317f722a25d1c13395ef6fa6bb3799cd6d088e",
                    "url": "https://github.com/twisted/python-info-action/commit/50228b7fc4ecef6feefec9d2be84a59d44aa15bb"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "6871cb07518bad00b4efa9dafc6425971b25dee7",
                    "message": "actually use the test argument",
                    "timestamp": "2021-03-01T16:57:51-05:00",
                    "tree_id": "f04896327226220d46d3f26a15b174fbae2c51b1",
                    "url": "https://github.com/twisted/python-info-action/commit/6871cb07518bad00b4efa9dafc6425971b25dee7"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "77a8d59cb03d09ee26a6664fa2c7439a00a788b7",
                    "message": "readme and -",
                    "timestamp": "2021-03-01T16:59:56-05:00",
                    "tree_id": "fe83d949062c7b4de7982a3fd1dfe02a94bdde70",
                    "url": "https://github.com/twisted/python-info-action/commit/77a8d59cb03d09ee26a6664fa2c7439a00a788b7"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "5aad86d985699709534a3564b6f4d72846ee8807",
                    "message": "another -",
                    "timestamp": "2021-03-01T17:01:58-05:00",
                    "tree_id": "50945651efa65453f8244b4a30932ced5fa1fc30",
                    "url": "https://github.com/twisted/python-info-action/commit/5aad86d985699709534a3564b6f4d72846ee8807"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "0bb6312a687b12697c7f830b9146c23c8944c1bc",
                    "message": "allow any pip version",
                    "timestamp": "2021-03-01T17:07:14-05:00",
                    "tree_id": "c33fb422e72af9e32b6278ea6c5882084ccbd773",
                    "url": "https://github.com/twisted/python-info-action/commit/0bb6312a687b12697c7f830b9146c23c8944c1bc"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "32cb68f2babb392d4bc2865a99c6eeca2bbfaf2e",
                    "message": "again",
                    "timestamp": "2021-03-01T17:14:16-05:00",
                    "tree_id": "d7f52c60f593fc8b334f3a8d4a7c1412b5995a49",
                    "url": "https://github.com/twisted/python-info-action/commit/32cb68f2babb392d4bc2865a99c6eeca2bbfaf2e"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "noreply@github.com",
                        "name": "GitHub",
                        "username": "web-flow"
                    },
                    "distinct": false,
                    "id": "6e85812f62177681379d23207a6cc46be3af8124",
                    "message": "Update README.rst",
                    "timestamp": "2021-03-11T23:59:51-05:00",
                    "tree_id": "80ec800e444d9f2b7d3cf160f3ffb75417882464",
                    "url": "https://github.com/twisted/python-info-action/commit/6e85812f62177681379d23207a6cc46be3af8124"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "distinct": false,
                    "id": "44e67191e350e61ab8d17b48ac4c36a8a81b3dad",
                    "message": "add test with a tox environment",
                    "timestamp": "2021-03-13T15:22:18-05:00",
                    "tree_id": "6d5057a3c00069e47d80b6f94ff9304267835f06",
                    "url": "https://github.com/twisted/python-info-action/commit/44e67191e350e61ab8d17b48ac4c36a8a81b3dad"
                },
                {
                    "author": {
                        "email": "sda@fstab.net",
                        "name": "Kyle Altendorf",
                        "username": "altendky"
                    },
                    "committer": {
                        "email": "noreply@github.com",
                        "name": "GitHub",
                        "username": "web-flow"
                    },
                    "distinct": false,
                    "id": "49042d6852bce250821e1e91d8cea9e7d4dd5f81",
                    "message": "Merge pull request #8 from altendky/python_path_as_a_parameter",
                    "timestamp": "2021-03-13T15:29:09-05:00",
                    "tree_id": "6d5057a3c00069e47d80b6f94ff9304267835f06",
                    "url": "https://github.com/twisted/python-info-action/commit/49042d6852bce250821e1e91d8cea9e7d4dd5f81"
                }
            ],
            "compare": "https://github.com/twisted/python-info-action/compare/bd29f7428500...49042d6852bc",
            "created": false,
            "deleted": false,
            "forced": false,
            "head_commit": {
                "author": {
                    "email": "sda@fstab.net",
                    "name": "Kyle Altendorf",
                    "username": "altendky"
                },
                "committer": {
                    "email": "noreply@github.com",
                    "name": "GitHub",
                    "username": "web-flow"
                },
                "distinct": false,
                "id": "49042d6852bce250821e1e91d8cea9e7d4dd5f81",
                "message": "Merge pull request #8 from altendky/python_path_as_a_parameter",
                "timestamp": "2021-03-13T15:29:09-05:00",
                "tree_id": "6d5057a3c00069e47d80b6f94ff9304267835f06",
                "url": "https://github.com/twisted/python-info-action/commit/49042d6852bce250821e1e91d8cea9e7d4dd5f81"
            },
            "organization": {
                "avatar_url": "https://avatars.githubusercontent.com/u/716546?v=4",
                "description": "",
                "events_url": "https://api.github.com/orgs/twisted/events",
                "hooks_url": "https://api.github.com/orgs/twisted/hooks",
                "id": 716546,
                "issues_url": "https://api.github.com/orgs/twisted/issues",
                "login": "twisted",
                "members_url": "https://api.github.com/orgs/twisted/members{/member}",
                "node_id": "MDEyOk9yZ2FuaXphdGlvbjcxNjU0Ng==",
                "public_members_url": "https://api.github.com/orgs/twisted/public_members{/member}",
                "repos_url": "https://api.github.com/orgs/twisted/repos",
                "url": "https://api.github.com/orgs/twisted"
            },
            "pusher": {
                "email": "sda@fstab.net",
                "name": "altendky"
            },
            "ref": "refs/tags/v1",
            "repository": {
                "archive_url": "https://api.github.com/repos/twisted/python-info-action/{archive_format}{/ref}",
                "archived": false,
                "assignees_url": "https://api.github.com/repos/twisted/python-info-action/assignees{/user}",
                "blobs_url": "https://api.github.com/repos/twisted/python-info-action/git/blobs{/sha}",
                "branches_url": "https://api.github.com/repos/twisted/python-info-action/branches{/branch}",
                "clone_url": "https://github.com/twisted/python-info-action.git",
                "collaborators_url": "https://api.github.com/repos/twisted/python-info-action/collaborators{/collaborator}",
                "comments_url": "https://api.github.com/repos/twisted/python-info-action/comments{/number}",
                "commits_url": "https://api.github.com/repos/twisted/python-info-action/commits{/sha}",
                "compare_url": "https://api.github.com/repos/twisted/python-info-action/compare/{base}...{head}",
                "contents_url": "https://api.github.com/repos/twisted/python-info-action/contents/{+path}",
                "contributors_url": "https://api.github.com/repos/twisted/python-info-action/contributors",
                "created_at": 1606495859,
                "default_branch": "main",
                "deployments_url": "https://api.github.com/repos/twisted/python-info-action/deployments",
                "description": "A GitHub Actions action for printing Python environment information",
                "disabled": false,
                "downloads_url": "https://api.github.com/repos/twisted/python-info-action/downloads",
                "events_url": "https://api.github.com/repos/twisted/python-info-action/events",
                "fork": false,
                "forks": 1,
                "forks_count": 1,
                "forks_url": "https://api.github.com/repos/twisted/python-info-action/forks",
                "full_name": "twisted/python-info-action",
                "git_commits_url": "https://api.github.com/repos/twisted/python-info-action/git/commits{/sha}",
                "git_refs_url": "https://api.github.com/repos/twisted/python-info-action/git/refs{/sha}",
                "git_tags_url": "https://api.github.com/repos/twisted/python-info-action/git/tags{/sha}",
                "git_url": "git://github.com/twisted/python-info-action.git",
                "has_downloads": true,
                "has_issues": true,
                "has_pages": false,
                "has_projects": true,
                "has_wiki": true,
                "homepage": null,
                "hooks_url": "https://api.github.com/repos/twisted/python-info-action/hooks",
                "html_url": "https://github.com/twisted/python-info-action",
                "id": 316555110,
                "issue_comment_url": "https://api.github.com/repos/twisted/python-info-action/issues/comments{/number}",
                "issue_events_url": "https://api.github.com/repos/twisted/python-info-action/issues/events{/number}",
                "issues_url": "https://api.github.com/repos/twisted/python-info-action/issues{/number}",
                "keys_url": "https://api.github.com/repos/twisted/python-info-action/keys{/key_id}",
                "labels_url": "https://api.github.com/repos/twisted/python-info-action/labels{/name}",
                "language": "Python",
                "languages_url": "https://api.github.com/repos/twisted/python-info-action/languages",
                "license": {
                    "key": "mit",
                    "name": "MIT License",
                    "node_id": "MDc6TGljZW5zZTEz",
                    "spdx_id": "MIT",
                    "url": "https://api.github.com/licenses/mit"
                },
                "master_branch": "main",
                "merges_url": "https://api.github.com/repos/twisted/python-info-action/merges",
                "milestones_url": "https://api.github.com/repos/twisted/python-info-action/milestones{/number}",
                "mirror_url": null,
                "name": "python-info-action",
                "node_id": "MDEwOlJlcG9zaXRvcnkzMTY1NTUxMTA=",
                "notifications_url": "https://api.github.com/repos/twisted/python-info-action/notifications{?since,all,participating}",
                "open_issues": 3,
                "open_issues_count": 3,
                "organization": "twisted",
                "owner": {
                    "avatar_url": "https://avatars.githubusercontent.com/u/716546?v=4",
                    "email": null,
                    "events_url": "https://api.github.com/users/twisted/events{/privacy}",
                    "followers_url": "https://api.github.com/users/twisted/followers",
                    "following_url": "https://api.github.com/users/twisted/following{/other_user}",
                    "gists_url": "https://api.github.com/users/twisted/gists{/gist_id}",
                    "gravatar_id": "",
                    "html_url": "https://github.com/twisted",
                    "id": 716546,
                    "login": "twisted",
                    "name": "twisted",
                    "node_id": "MDEyOk9yZ2FuaXphdGlvbjcxNjU0Ng==",
                    "organizations_url": "https://api.github.com/users/twisted/orgs",
                    "received_events_url": "https://api.github.com/users/twisted/received_events",
                    "repos_url": "https://api.github.com/users/twisted/repos",
                    "site_admin": false,
                    "starred_url": "https://api.github.com/users/twisted/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/twisted/subscriptions",
                    "type": "Organization",
                    "url": "https://api.github.com/users/twisted"
                },
                "private": false,
                "pulls_url": "https://api.github.com/repos/twisted/python-info-action/pulls{/number}",
                "pushed_at": 1615667664,
                "releases_url": "https://api.github.com/repos/twisted/python-info-action/releases{/id}",
                "size": 41,
                "ssh_url": "git@github.com:twisted/python-info-action.git",
                "stargazers": 0,
                "stargazers_count": 0,
                "stargazers_url": "https://api.github.com/repos/twisted/python-info-action/stargazers",
                "statuses_url": "https://api.github.com/repos/twisted/python-info-action/statuses/{sha}",
                "subscribers_url": "https://api.github.com/repos/twisted/python-info-action/subscribers",
                "subscription_url": "https://api.github.com/repos/twisted/python-info-action/subscription",
                "svn_url": "https://github.com/twisted/python-info-action",
                "tags_url": "https://api.github.com/repos/twisted/python-info-action/tags",
                "teams_url": "https://api.github.com/repos/twisted/python-info-action/teams",
                "trees_url": "https://api.github.com/repos/twisted/python-info-action/git/trees{/sha}",
                "updated_at": "2021-03-13T20:29:12Z",
                "url": "https://github.com/twisted/python-info-action",
                "watchers": 0,
                "watchers_count": 0
            },
            "sender": {
                "avatar_url": "https://avatars.githubusercontent.com/u/543719?v=4",
                "events_url": "https://api.github.com/users/altendky/events{/privacy}",
                "followers_url": "https://api.github.com/users/altendky/followers",
                "following_url": "https://api.github.com/users/altendky/following{/other_user}",
                "gists_url": "https://api.github.com/users/altendky/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/altendky",
                "id": 543719,
                "login": "altendky",
                "node_id": "MDQ6VXNlcjU0MzcxOQ==",
                "organizations_url": "https://api.github.com/users/altendky/orgs",
                "received_events_url": "https://api.github.com/users/altendky/received_events",
                "repos_url": "https://api.github.com/users/altendky/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/altendky/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/altendky/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/altendky"
            }
        },
        "server_url": "https://github.com",
        "api_url": "https://api.github.com",
        "graphql_url": "https://api.github.com/graphql",
        "workspace": "/home/runner/work/python-info-action/python-info-action",
        "action": "self1",
        "event_path": "/home/runner/work/_temp/_github_workflow/event.json",
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
