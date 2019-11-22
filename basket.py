"""
HackerRank challenge: Given an input file containing a list of game scores in
chronological order, find the number of times the player beat their high score
and beat their low score.

File format:
<number of games played>
<game scores separated by spaces>

usage: basket.py [-h] input_file

positional arguments:
  input_file

  optional arguments:
    -h, --help  show this help message and exit

"""

import sys
import argparse


DEBUG = False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    with open(args.input_file, 'r') as fd:
        next(fd)
        scores = (int(s) for s in fd.readline().split())
        result = get_num_bw(scores)
        print(result[0], result[1])

def get_num_bw(scores):
    if not scores:
        return 0, 0
    min_s = max_s = next(scores)
    num_best = num_worst = 0

    for s in scores:
        if s < min_s:
            min_s = s
            if DEBUG: print("update min_s to {}".format(min_s))
            num_worst += 1
        if s > max_s:
            max_s = s
            if DEBUG: print("update max_s to {}".format(max_s))
            num_best += 1
    return num_best, num_worst

if __name__ == "__main__":
    main()
