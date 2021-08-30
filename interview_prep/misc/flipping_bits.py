# Hackerrank Problem
# 
# Jumping the clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds

from typing import List
import sys

def flip_bits(n:int) -> int:
    num_bits = 32
    mask = 2**num_bits - 1
    return n ^ mask
def main():

    
    print(flip_bits(1))
    print(list(range(3,100,2)))
    return 0


if __name__ == "__main__":
    main()
