#!/usr/bin/python3
"""
data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & mask1) and (byte & mask2) == 0:
                return False
            elif (byte & mask1) and (byte & mask2):
                num_bytes += 1
                if (byte & 0xF0) == 0xE0:
                    num_bytes = 2
                elif (byte & 0xF8) == 0xF0:
                    num_bytes = 3
                elif (byte & 0xE0) == 0xC0:
                    num_bytes = 1
                else:
                    return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
