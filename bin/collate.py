"""
    'Brief description of what the script does.'
"""
import argparse
import csv
import string
from collections import Counter
import utilities as util


def count_words(reader):
    contents = reader.read()
    words = contents.split()
    word_list = [word.strip(string.punctuation).lower() for word in words]
    word_counts = Counter(word_list)
    return word_counts


def update_counts(reader, word_counts):
    for word, count in csv.reader(reader):
        word_counts[word] += int(count)


def main(args):
    """Run the command line program."""
    word_counts = Counter()
    for fname in args.infile:
        with open(fname, 'r') as reader:
            update_counts(reader, word_counts)
    util.collection_to_csv(word_counts, num=args.num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    # '*' to tell argparse that we will accept zero or more filenames
    parser.add_argument('infile', type=str,
                        nargs='*', help='Input file name')
    parser.add_argument('-n', '--num', type=int,
                        default=None, help='Output the most common words')
    args = parser.parse_args()
    main(args)
