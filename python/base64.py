"""
Python 3 script to encode binary data using base64 and decode it back.

To encode data, the script breaks it into chunks of six bits and uses the
mapping defined in enc_map. If fewer than six bits are remaining in the last
chunk, the script adds two or four zero bits to the last chunk as necessary
and appends one or two 'equals' signs to the encoding respectively.

To decode data, the script breaks it into chunks of four bytes and then reads
six bits at a time from the data, using a reversed enc_map to look up the
original bytes. If equals signs are present, they are treated as two or four
zero bits in the data.
"""

import re

enc_map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

DEBUG = False

def _generate_decode_map():
    return {c: i for i, c in enumerate(enc_map)}  # dict comprehension!

"https://stackoverflow.com/a/312464"
def _chunker(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]

def bin_to_b64(data):
    result = ""
    bits = "".join(format(b, "08b") for b in data)
    if DEBUG: print("bits", bits)
    start = 0
    while start < len(bits):
        fill_len = 0
        if len(bits) - start < 6:
            fill_len = 6 - (len(bits) - start)
        if DEBUG: print("fill_len", fill_len)
        bin_sect = bits[start:start+6] + '0' * fill_len  # fill with '', '00', or '0000'
        if DEBUG: print(bin_sect, int(bin_sect, 2))
        result += enc_map[int(bin_sect, 2)]
        result += '=' * (fill_len // 2)  # 0, 1, or 2
        start += 6
    return result

def b64_to_bin(b64):
    b64 = re.sub(r"\s+", "", b64, flags=re.UNICODE)  # remove whitespace
    bin_encoded_data = ""
    result = ""
    dec_map = _generate_decode_map()
    for group in _chunker(b64, 4):
        pad_ndx = group.find('=')
        pad_ndx = len(group) if pad_ndx == -1 else pad_ndx
        decoded_bytes = (dec_map[c] for c in group[:pad_ndx])
        bin_sect = "".join(format(b, "06b") for b in decoded_bytes)
        bin_pad_len = (len(group) - pad_ndx) * 4  # 4 * quantity of '='
        bin_pad = bin_pad_len * '0'
        bin_encoded_data += bin_sect + bin_pad
    for group in _chunker(bin_encoded_data, 8):
        result += chr(int("".join(group), 2))
    return result

print(bin_to_b64(b"Man"))  # TWFu
print(bin_to_b64(b"Ma"))  # TWE=
print(bin_to_b64(b"M"))  # TQ==
print(b64_to_bin("TWFu"))
print(b64_to_bin("TWE="))
print(b64_to_bin("TQ=="))
