import argparse
import os.path
import csv
import pandas as pd

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--file', dest='filename',
                    help='Please provide a csv')

args = parser.parse_args()

OUTFILE ="twg_data.csv"


def run(filename):
    df = pd.read_csv(filename, index_col=None)

    point3 = df.dropna(thresh=10)
    clean = point3.fillna(0)
    test = clean.groupby(['cat1', 'cat2'])['cpercentage'].mean()

    test.to_csv(OUTFILE)


if __name__ == "__main__":
    run(args.filename)
