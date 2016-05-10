
import yaml
import pprint

from tests.test_constructor import MyDumper, MyLoader, _load_code, _serialize_value

def test_representer_types(code_filename, verbose=False):
    for allow_unicode in [False, True]:
        for encoding in ['utf-8', 'utf-16-be', 'utf-16-le']:
            native1 = _load_code(open(code_filename, 'rb').read())
            native2 = None
            try:
                output = yaml.dump(native1, Dumper=MyDumper,
                            allow_unicode=allow_unicode, encoding=encoding)
                native2 = yaml.load(output, Loader=MyLoader)
                try:
                    if native1 == native2:
                        continue
                except TypeError:
                    pass
                value1 = _serialize_value(native1)
                value2 = _serialize_value(native2)
                if verbose:
                    print("SERIALIZED NATIVE1:")
                    print(value1)
                    print("SERIALIZED NATIVE2:")
                    print(value2)
                assert value1 == value2, (native1, native2)
            finally:
                if verbose:
                    print("NATIVE1:")
                    pprint.pprint(native1)
                    print("NATIVE2:")
                    pprint.pprint(native2)
                    print("OUTPUT:")
                    print(output)

test_representer_types.unittest = ['.code']
