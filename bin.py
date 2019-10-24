"""
Python 3 script to convert decimal numbers to binary strings and back.
Decimal to binary conversion only works with positive numbers.
"""

def dec_to_bin(num):
    ans = ""
    while num > 0:
        if num % 2 != 0:  # even
            ans = "1" + ans
            num -= 1
        else:  # odd
            ans = "0" + ans
        num //= 2
    return ans

def bin_to_dec(b):
    result = 0
    place_val = 1
    for n in b[::-1]:
        result += place_val * int(n)
        place_val *= 2
    return result
    
res = dec_to_bin(int(input()))
print(res)
print(bin_to_dec(res))
