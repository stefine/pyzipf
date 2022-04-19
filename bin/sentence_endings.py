import argparse


def main(reader):
    contents = reader.read()
    for stop in ['.', '?', '!']:
        print(f"Number of {stop} is {contents.count(stop)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-', help="Infile input")
    args = parser.parse_args()
    main(args.infile)
