"""
Python 3 script to do a character-by-character diff between two files and
output only the differing characters. Used for a PicoCTF challenge.

usage: chardiff.py [-h] file1 file2

positional arguments:
  file1
    file2

    optional arguments:
      -h, --help  show this help message and exit

"""

import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file1')
    parser.add_argument('file2')
    args = parser.parse_args()

    str1 = bytearray()
    str2 = bytearray()
    with open(args.file1, 'rb') as fd1, open(args.file2, 'rb') as fd2:
        while True:
            c1 = fd1.read(1)
            c2 = fd2.read(1)
            if not c1 and not c2:
                break
            if c1 != c2:
                print(c1)
                print(c2)
                str1.extend(c1 or b"")
                str2.extend(c2 or b"")
    print("File 1:\n\n{}\n\n".format(repr(str1)[12:-1]))
    print("File 2:\n\n{}".format(repr(str2)[12:-1]))
