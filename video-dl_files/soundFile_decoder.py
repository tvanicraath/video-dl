#!/usr/bin/python
#thanks to laszlo.nu. Source: http://www.laszlo.nu/post/2567437671/reversing-wordpress-audioplayer-url-obfuscation

import sys

def int2bin(n):
    assert n >= 0, "Number must be positive"
    res = ""
    if n == 0: return "0"
    while True:
        if n == 0:
            return res
        elif n % 2 == 0:
            res = "0" + res
        else:
            res = "1" + res
            n -= 1
        n /= 2

def decode(source):
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"
    binary = ""

    for char in source:
        code = key.find(char) # look up each char in the code key
        binary += int2bin(code).rjust(6, "0") # append char index as a six bit binary string
    
    chunks = [] 
    # split string into segments of length 8
    while len(binary) > 0:
        chunks.append(binary[:8]) 
        binary = binary[8:]

    chars = [chr(int(x, 2)) for x in chunks] # convert the segments to chars
    return "".join(chars)

# http://www.mabd.se/?p=682
#test = sys.argv[1]
print(decode("7A2113827D473A718C78693B856C112BFADE81DD"))

