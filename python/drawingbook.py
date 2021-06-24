"""
HackerRank challenge: Given an input file given a number of pages and target
page, determine the minimum number of single page turns needed to arrive at the
target page in a booklet. The reader can start at the beginning or end of the
booklet. Opening to the first or last page is not counted.

File format:
<number of pages>
<page to turn to>

usage: drawingbook.py [-h] input_file

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
        pages = int(fd.readline())
        target = int(fd.readline())
        result = page_count(pages, target)
        print(result)

def page_count(pages, target):
    def is_even(n):
        return n % 2 == 0

    if target <= pages // 2: # left side
        return target // 2
    else: # right side
        if is_even(pages):
            return (pages - target + 1) // 2  # round up
        else:
            return (pages - target) // 2  # round down


def page_count(pages, target):
    num_groups = pages // 2 + 1


if __name__ == "__main__":
    main()
