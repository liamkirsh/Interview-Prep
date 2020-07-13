"""
HackerRank challenge: Given an input file containing an array of integers, find
the maximum number of integers you can select such that the absolute difference
between any two of the chosen integers is less than or equal to 1.

File format:
<size of the array>
<integer> <integer> <integer> ...

usage: pickingNumbers.py [-h] input_file

positional arguments:
  input_file

  optional arguments:
    -h, --help  show this help message and exit

"""

import argparse

DEBUG = False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    with open(args.input_file, 'r') as fd:
        next(fd)
        ary = [int(s) for  s in fd.readline().split()]
        result = get_subary_len(ary)
        print(result)

def get_subary_len(ary):
    max_len = -1

    # Create buckets to track how many times each number occurs in the array
    tracking_ary = [0] * 99  # 0 < a[i] < 100
    for n in ary:  # O(n)
        tracking_ary[n - 1] += 1

    # Find the highest sum value among adjacent buckets
    for i in range(1, len(tracking_ary)):  # O(1)
        cur_subary_len = tracking_ary[i - 1] + tracking_ary[i]
        if cur_subary_len > max_len:
            max_len = cur_subary_len
    return max_len


if __name__ == "__main__":
    main()
