"""Templating helpers.


"""


import shutil
import os
from jinja2 import Template

from uswarm.tools import expandpath, relpath

# -----------------------------------------------
# file helpers
# -----------------------------------------------
def safe_copy(dest, src, overwrite=False, **ctx):
    """Copy files from src to dest.
    - do not overwrite existing files by default
    - expand files using jinja2

    """
    src = expandpath(src)
    dest = expandpath(dest)
    os.makedirs(dest, exist_ok=True)
    for root, folders, files in os.walk(src):
        relroot = relpath(root, src)
        for name in folders:
            path = os.path.join(dest, relroot, name)
            os.makedirs(path, exist_ok=True)
        for name in files:
            path0 = os.path.join(root, name)
            path1 = os.path.join(dest, relroot, name)
            if overwrite or not os.access(path1, os.F_OK):
                try:
                    source = open(path0, "r").read()
                    try:
                        print(f" - {name:15} expanding")
                        T = Template(source)
                        # print(ctx)
                        result = T.render(**ctx)
                    except Exception as why:
                        print(
                            f"ERROR: {why} at line: {why.lineno}, ignoring this file."
                        )
                        continue
                        foo = 1
                    open(path1, "w").write(result)

                except UnicodeDecodeError as why:
                    print(f" - {name:15} binary coping")
                    # source = open(path0, 'rb').read()
                    # open(path1, 'wb').write(result)
                    shutil.copy(path0, path1)
