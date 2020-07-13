"""
HackerRank challenge: Given a budget, a list of keyboard prices, and a list of
USB drive prices, find the most expensive set of one keyboard and one USB drive
that Monica can buy given her budget. Prints the maximum price or -1 if there
is no possible combination within her budget.

File format:
<budget> <number of keyboard models> <number of USB models>
<prices of each keyboard model separated by spaces>
<prices of each USB drive model separated by spaces>

usage: electronics.py [-h] input_file

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
        budget = int(fd.readline().split()[0])
        kboard_p = [int(x) for x in fd.readline().split()]
        usb_p = [int(x) for x in fd.readline().split()]
        result = get_money_spent(budget, kboard_p, usb_p)
        print(result)

def get_money_spent(budget, keyboard_p, usb_p):
    keyboard_p.sort()
    usb_p.sort()
    if DEBUG:
        print("kboard prices", keyboard_p)
        print("usb prices", usb_p)

    cur_max = -1
    for k_n, k_val in enumerate(keyboard_p):
        if DEBUG: print("checking keyboard price", k_val)
        if k_val >= budget:
            break
        for u_n, u_val in enumerate(usb_p):
            if DEBUG: print("checking usb price", u_val)
            if k_val + u_val > budget:
                if DEBUG:
                    print("products exceed budget")
                break
            elif k_val + u_val > cur_max:
                cur_max = k_val + u_val
    return cur_max

if __name__ == "__main__":
    main()
