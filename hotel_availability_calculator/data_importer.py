import csv


def import_from_file(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='#')

