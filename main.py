import sys
import pandas as pd


def split_csv(file, count):
    for i, chunk in enumerate(pd.read_csv(file, chunksize=count)):
        chunk.to_csv('chunk_{}.csv'.format(i), index=False)


if __name__ == '__main__':
    # Example:
    #   python3 main.py my_file.csv 100
    split_csv(sys.argv[1], int(sys.argv[2]))
