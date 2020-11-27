from __future__ import print_function

import io
import os
import struct
import subprocess
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    NativeIO = io.BytesIO
elif PY3:
    NativeIO = io.StringIO
else:
    raise Exception("Unsupported Python version: {}".format(sys.version))


class Output:
    def __init__(self):
        self.chunks = []

    def print(self, *args, **kwargs):
        file = NativeIO()
        print(*args, file=file, **kwargs)
        chunk = file.getvalue()
        sys.stdout.write(chunk)
        self.chunks.extend(chunk)

    def heading(self, name):
        self.print()
        self.print(name)
        self.print("=" * len(name))
        self.print()

    def value(self):
        return "".join(chunk for chunk in self.chunks)

output = Output()

output.heading("Python Details")

output.print("sys.version              :", sys.version)
output.print("sys.prefix               :", sys.prefix)
output.print("sys.exec_prefix          :", sys.exec_prefix)
output.print("sys.executable           :", sys.executable)
output.print("struct.calcsize(\"P\") * 8 :", struct.calcsize("P") * 8)

output.heading("Environment Variables")

environment = dict(os.environ)

maximum_key_length = max(
    len(repr(key))
    for key in environment.keys()
)

for name, value in sorted(environment.items()):
    line = "{: <{}} : {}".format(
        repr(name),
        maximum_key_length,
        repr(value),
    )
    output.print(line)

output.heading("Installed Packages")

with open(os.devnull, 'w') as devnull:
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

freeze.strip()
if len(freeze) > 0:
    output.print(freeze)
else:
    output.print("None")

output_path = os.environ.get("ACTION_FILE_PATH", "")
if output_path != "":
    with open(output_path, 'w') as f:
        f.write(output.value())
