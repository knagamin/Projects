#!/usr/bin/env python3
# conding: utf-8
import math

"""
numbers module

Modules for projects's solutions
"""

def find_pi_n_digits(n):
   pi_str = str(math.pi)

   return int(pi_str[n+1])
