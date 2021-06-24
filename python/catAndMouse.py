"""
HackerRank challenge: Given an input file containing a list of queries, such
that each query details the positions of two cats and a mouse on a line,
determine which cat will reach the mouse first if they move at the same speed.

File format:
<number of queries>
<cat A location> <cat B location> <mouse location>
[...]

usage: catAndMouse.py [-h] input_file

positional arguments:
  input_file

  optional arguments:
    -h, --help  show this help message and exit

"""

import sys
import argparse

DEBUG = True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    with open(args.input_file, 'r') as fd:
        next(fd)
        for query in fd:
            catA, catB, mouse = [int(s) for s in query.split()]
            result = get_winner(catA, catB, mouse)
            print(result)


def get_winner(catA, catB, mouse):
    distA = abs(catA - mouse)
    distB = abs(catB - mouse)
    if distA == distB:
        return "Mouse C"
    elif distA < distB:
        return "Cat A"
    else:
        return "Cat B"


if __name__ == "__main__":
    main()
