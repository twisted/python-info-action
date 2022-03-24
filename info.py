from __future__ import print_function

import io
import json
import os
import struct
import subprocess
import sys
import sysconfig

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
CONTEXT_PREFIX = "_PYTHON_INFO_ACTION_CONTEXT_"

if PY2:
    NativeIO = io.BytesIO
elif PY3:
    NativeIO = io.StringIO
else:
    raise Exception("Unsupported Python version: {}".format(sys.version))


class Output:
    def __init__(self):
        self.chunks = []
        self.heading_marks = ["=", "-"]
        self.group_open = False

    def print(self, *args, **kwargs):
        file = NativeIO()
        print(*args, file=file, **kwargs)
        chunk = file.getvalue()
        sys.stdout.write(chunk)
        self.chunks.extend(chunk)

    def heading(self, name, level):
        self.print()

        if level == 0:
            if self.group_open:
                # The final end group is being intentionally ignored at present.
                sys.stdout.write("::endgroup::\n")
            sys.stdout.write("::group::{name}\n".format(name=name))

        self.print(name)
        self.print(self.heading_marks[level] * len(name))
        self.print()

        self.group_open = True

    def value(self):
        return "".join(chunk for chunk in self.chunks)

    def print_mapping(self, mapping):
        maximum_key_length = max(len(repr(key)) for key in mapping.keys())

        for name, value in sorted(mapping.items()):
            line = "{: <{}} : {}".format(
                repr(name),
                maximum_key_length,
                repr(value),
            )
            self.print(line)


output = Output()

environment = dict(os.environ)

output.heading("Python Details", 0)

output.print("sys.version              :", sys.version)
output.print("sys.prefix               :", sys.prefix)
output.print("sys.exec_prefix          :", sys.exec_prefix)
output.print("sys.executable           :", sys.executable)
output.print('struct.calcsize("P") * 8 :', struct.calcsize("P") * 8)

output.heading("Python Configuration", 0)

output.print("sysconfig.get_platform()       :", sysconfig.get_platform())
output.print("sysconfig.get_python_version() :", sysconfig.get_python_version())

output.heading("Paths", level=1)
output.print_mapping(sysconfig.get_paths())

output.heading("Variables", level=1)
output.print_mapping(sysconfig.get_config_vars())

output.heading("Environment Variables", 0)

output.print_mapping(
    mapping={
        key: value
        for key, value in environment.items()
        if not key.startswith(CONTEXT_PREFIX)
    },
)

output.heading("Installed Packages", 0)

with open(os.devnull, "w") as devnull:
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "--no-python-version-warning"],
            stdout=devnull,
            stderr=devnull,
        )
    except subprocess.CalledProcessError:
        supports_no_warning = False
    else:
        supports_no_warning = True

arguments = []
if supports_no_warning:
    arguments.append("--no-python-version-warning")

freeze = subprocess.check_output(
    [sys.executable, "-m", "pip", "freeze", "--all"] + arguments,
)

if PY3:
    freeze = freeze.decode()

freeze = freeze.strip()
freeze = freeze.replace("\r\n", "\n")
if len(freeze) > 0:
    output.print(freeze)
else:
    output.print("None")

output.heading("Workflow Details", 0)

contexts = {
    key[len(CONTEXT_PREFIX):]: json.loads(value)
    for key, value in environment.items()
    if key.startswith(CONTEXT_PREFIX)
}

for name, value in contexts.items():
    output.heading(name, level=1)
    output.print(json.dumps(value, indent=4))

output_path = os.environ.get("ACTION_FILE_PATH", "")
if output_path != "":
    with open(output_path, "w") as f:
        f.write(output.value())
