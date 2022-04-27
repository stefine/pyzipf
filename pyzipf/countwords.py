"""
    'Brief description of what the script does.'
"""
import argparse
import string
from collections import Counter
from pyzipf import utilities as util


def count_words(reader):
    contents = reader.read()
    words = contents.split()
    word_list = [word.strip(string.punctuation).lower() for word in words]
    word_counts = Counter(word_list)
    return word_counts


def main():
    """Run the command line program."""
    args = parse_command_line()
    word_counts = count_words(args.infile)
    util.collection_to_csv(word_counts, num=args.num)


def parse_command_line():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('-n', '--num', type=int,
                        default=None, help='Output the most common words')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
