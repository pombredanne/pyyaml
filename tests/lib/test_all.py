
import sys, yaml, test_appliance

def main(args=None):
    collections = []
    import test_yaml
    collections.append(test_yaml)
    test_appliance.run(collections, args)

if __name__ == '__main__':
    main()
