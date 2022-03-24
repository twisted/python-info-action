from __future__ import print_function

import argparse
import os
import re
import sys


def parse_arguments(arguments):
    parser = argparse.ArgumentParser(
        description="Test the python-info-action output",
    )
    
    parser.add_argument(
        "--path",
        required=True,
        help="The path to the action's output file.",
    )

    parser.add_argument(
        "--package",
        required=False,
        nargs=2,
        action='append',
        default=[],
        help="Argument and version pair.  You can pass multiple times.",
    )

    parser.add_argument(
        "--sys-prefix",
        required=False,
        default=sys.prefix,
        help=(
            "The sys.prefix to check for in case the tests are run in"
            " an env other than the action."
        ),
    )

    return parser.parse_args(args=arguments)


def main(raw_arguments):
    arguments = parse_arguments(arguments=raw_arguments)
    with open(arguments.path) as f:
        output = f.read()

    secret_text = "neverseethis"

    assert secret_text not in output
    assert secret_text == os.environ["A_SECRET"]

    relative_path = os.path.relpath(arguments.path, os.getcwd())

    assert re.search(
        "^'ACTION_FILE_PATH' +: '{}'$".format(re.escape(relative_path)),
        output,
        re.MULTILINE,
    )

    assert re.search(
        "^sys.prefix +: {}$".format(re.escape(arguments.sys_prefix)),
        output,
        re.MULTILINE,
    )

    assert re.search(
        "^'platstdlib' +: ",
        output,
        re.MULTILINE,
    )

    assert re.search(
        "^'Py_DEBUG' +: [01]$",
        output,
        re.MULTILINE,
    )

    arguments.package.append(("pip", None))

    for name, version in arguments.package:
        if version is None:
            re_version = ".*"
        else:
            re_version = re.escape(version)
        print("checking for: {}, {}".format(name, version))
        assert re.search(
            "^{}=={}$".format(re.escape(name), re_version),
            output,
            re.MULTILINE,
        )


if __name__ == "__main__":
    sys.exit(main(raw_arguments=sys.argv[1:]))
