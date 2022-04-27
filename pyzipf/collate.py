"""
    'Brief description of what the script does.'
"""
import argparse
import csv
import string
from collections import Counter
import utilities as util
import logging


def count_words(reader):
    contents = reader.read()
    words = contents.split()
    word_list = [word.strip(string.punctuation).lower() for word in words]
    word_counts = Counter(word_list)
    return word_counts


def update_counts(reader, word_counts):
    for word, count in csv.reader(reader):
        word_counts[word] += int(count)


def process_file(fname, word_counts):
    logging.debug(f'Reading in {fname}...')
    if fname[-4:] != '.csv':
        msg = util.ERRORS['not_csv_suffix'].format(fname=fname)
        raise OSError(msg)
    with open(fname, 'r') as reader:
        logging.debug('Computing word counts...')
        update_counts(reader, word_counts)


def main(args):
    """Run the command line program."""
    log_level = logging.DEBUG if args.verbose else logging.WARNING
    logging.basicConfig(level=log_level, filename=args.logfile)

    word_counts = Counter()
    logging.info('Processing files...')

    for fname in args.infile:
        try:
            process_file(fname, word_counts)
        except FileNotFoundError:
            msg = f'{fname} not processed: File does not exist'
            logging.warning(msg)
        except PermissionError:
            msg = f'{fname} not processed: No read permission'
            logging.warning(msg)
        except Exception as error:
            msg = f'{fname} not processed: {error}'
            logging.warning()

    util.collection_to_csv(word_counts, num=args.num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    # '*' to tell argparse that we will accept zero or more filenames
    parser.add_argument('infile', type=str,
                        nargs='*', help='Input file name')
    parser.add_argument('-n', '--num', type=int,
                        default=None, help='Output the most common words')
    parser.add_argument('-v', '--verbose', action="store_true",
                        default=False, help='Change the logging level')
    parser.add_argument('-l', '--logfile', type=str,
                        default='collate.log', help='Edit the log file')
    args = parser.parse_args()
    main(args)
