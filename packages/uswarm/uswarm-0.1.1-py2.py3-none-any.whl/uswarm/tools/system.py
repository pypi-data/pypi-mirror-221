"""Helpers for dealing with system.

Processes
-----------------------

- [x] pid helpers
- [x] lsof



"""
import os
import re
import sh

from ..tools import parse_uri

# --------------------------------------------------
# File descriptor operations
# --------------------------------------------------


def lsof():
    "List Open Files."
    regexp = re.compile(r"/proc/(?P<pid>\d+)/fd/(?P<fd>\d+)$")
    for root, folder, files in os.walk("/proc"):
        for name in files:
            path = os.path.join(root, name)
            m = regexp.match(path)
            if m:
                d = m.groupdict()
                try:
                    d["path"] = path
                    filename = os.readlink(path)
                    # if file == '/dev/null' or \
                    # re.match(r'pipe:\[\d+\]', file) or \
                    # re.match(r'socket:\[\d+\]', file):
                    # foo = 1
                except OSError as err:
                    if err.errno == 2:
                        file = None
                    else:
                        raise (err)

                yield (filename, d)

                foo = 1


def iterate_fds(pid):
    """Iterate over the *fds* of a *pid* process."""
    dir = f"/proc/{pid}/fd"
    if not os.access(dir, os.R_OK | os.X_OK):
        return

    for fds in os.listdir(dir):
        for fd in fds:
            full_name = os.path.join(dir, fd)
            try:
                file = os.readlink(full_name)
                if (
                    file == "/dev/null"
                    or re.match(r"pipe:\[\d+\]", file)
                    or re.match(r"socket:\[\d+\]", file)
                ):
                    file = None
            except OSError as err:
                if err.errno == 2:
                    file = None
                else:
                    raise (err)

            yield (fd, file)


# --------------------------------------------------
# PID and Processes
# --------------------------------------------------
def pid_of(path):
    """iterate over processes returning info that match *path*."""
    for _path, result in lsof():
        if path == _path:
            yield result


def test_pid(pid):
    """Test if a PID exits."""
    try:
        pid = int(pid)
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


# --------------------------------------------------
# IP Helpers
# --------------------------------------------------

reg_ipv4_head = r"""(?imux)
\d+:\s+
(?P<iface>[^:]+)
"""

reg_ipv4_single = r"""(?imux)
inet\s+(?P<ipv4>\d+\.\d+\.\d+\.\d+)
(/(?P<maskv4>\d+))?
.*?
(?P<brdv4>\d+\.\d+\.\d+\.\d+)
"""


def get_ifaces():
    result = {}
    output = str(sh.ip("a"))

    current = None
    for line in sh.ip("a"):
        m = re.search(reg_ipv4_head, line)
        if m:
            current = m.groupdict()["iface"]
            continue
        if current:
            m = re.search(reg_ipv4_single, line)
            if m:
                result[current] = m.groupdict()
                current = None

    return result


# ------------------------------------------------
# parallel remote ssh execution
# ------------------------------------------------
def parallel_ssh_exec(urls, cmd, *args, **kw):
    """Performs a parallel execuion of a commmand
    using ssh on a list of remote hosts.
    """
    result = {}
    kwargs = dict(
        _bg=False,  # TODO: search in parallel
        _bg_exc=False,
        # _timeout=35,
        # password="1dvd", interact=ssh_interact,
    )
    kwargs.update(kw)
    for i, url in enumerate(urls):
        uri = parse_uri(url)
        user = uri["user"]
        if user:
            s = sh.ssh.bake(uri["host"], "-l", user)
        else:
            s = sh.ssh.bake(uri["host"])

        # s = s.bash.bake("-c")

        try:
            print(f"{url}: {cmd} {args} : {kwargs}")
            result[url] = getattr(s, cmd)(*args, **kwargs)
        except Exception as why:
            foo = 1

    return result


def parallel_ssh_exec_regexp(urls, regexp, cmd, *args, **kw):
    result = {}
    for url, output in parallel_ssh_exec(urls, cmd, *args, **kw).items():
        # print(f"{url}: {output}")
        holder = result.setdefault(url, list())
        for line in output:
            m = re.search(regexp, line)
            if m:
                d = m.groupdict()
                # print(d)
                holder.append(d)
    return result
