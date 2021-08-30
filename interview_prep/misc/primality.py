from typing import List
import sys, math

def primality(n):
    np = "Not prime"
    p = "Prime"
    if n < 2 or n %2 == 0:
        return np
    limit = int(math.sqrt(n))
    # print(n,limit)
    for i in range(3,limit+1,2):
        if n % i == 0:
            return np
    return p
def main():

    
    for i in range(20):
        print(i, primality((i)))
    return 0


if __name__ == "__main__":
    main()
