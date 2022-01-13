#!/usr/bin/python3
for x in range(1, 256):  # doing range from 1 as 0 is bad character
  print("\\x" + "{:02x}".format(x), end='')
print()