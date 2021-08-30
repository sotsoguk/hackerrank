# Hackerrank Problem
# 
# Jumping the clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds

from typing import List
import sys

def jtc_rec(clouds: List[int], idx, steps:int) ->int:
    # reach the end
    if idx == len(clouds) - 1:
        return steps
    # jump onto thunderhead or jump over the end
    if idx >= len(clouds) or clouds[idx] == 1:
        return sys.maxsize

    # recursivley compute the steps for 1 or 2 jumps
    return min(jtc_rec(clouds,idx+1,steps+1),jtc_rec(clouds,idx+2,steps+1))

def jump_the_clouds(clouds: List[int]) -> int:
    
    return jtc_rec(clouds,0,0)

def main():
    test1 = [0,0,1,0,0,1,0]
    test2 = [0,0,0,0,1,0]
    test3 = [0,1,0,0,0,1,0]
    print(jump_the_clouds((test2)))
    return 0


if __name__ == "__main__":
    main()
