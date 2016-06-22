import os
import os.path
import inspect
import sys


DATA = "tests/data"


def find_test_filenames(directory):
    filenames = {}
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            base, ext = os.path.splitext(filename)
            if base.endswith("-py2") and sys.version_info[0] == 3:
                continue
            elif base.endswith("-py3") and sys.version_info[0] == 2:
                continue
            filenames.setdefault(base, []).append(ext)
    filenames = sorted(filenames.items())
    return filenames


def pytest_generate_tests(metafunc):
    if getattr(metafunc.function, "unittest", []):
        params = []
        for base, exts in find_test_filenames(DATA):
            filenames = []
            for ext in metafunc.function.unittest:
                if ext not in exts:
                    break
                filenames.append(os.path.join(DATA, base + ext))
            else:
                skip_exts = getattr(metafunc.function, 'skip', [])
                for skip_ext in skip_exts:
                    if skip_ext in exts:
                        break
                else:
                    params.append(tuple(filenames))

        args, _, _, _ = inspect.getargspec(metafunc.function)
        args = [arg for arg in args if arg != "verbose"]

        metafunc.parametrize(args, params)
