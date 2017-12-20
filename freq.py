#!/usr/bin/env python2

# Albert was here

from __future__ import division
import sys

if len(sys.argv) != 2:
    print 'Usage:', sys.argv[0], '<corpus textfile>'
    exit(1)

filename = sys.argv[1]

# Create 256 element list and initialize to 0
counts = [0] * 256
total = 0

with open(filename) as f:
  for line in f:
      for c in line:
          total += 1
          counts[ord(c)] += 1

for i in range(256):
    print counts[i] / total
