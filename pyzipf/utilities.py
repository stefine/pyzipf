import csv
import sys

ERRORS = {
    'not_csv_suffix': '{fname}: File must end in .csv',
}

def collection_to_csv(collection, num):
    """Write collection of items and counts in csv format."""
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    writer = csv.writer(sys.stdout)
    writer.writerows(collection[0:num])
