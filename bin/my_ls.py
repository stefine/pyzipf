import argparse
import glob


def main(args):
    dir = args.dir if args.dir[-1] == '/' else args.dir + '/'
    path = dir + '*.' + args.suffix
    for item in sorted(glob.glob(path)):
        print(item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, help="Directory")
    parser.add_argument('suffix', type=str, help="File suffix (e.g. py, sh)")
    args = parser.parse_args()
    main(args)
