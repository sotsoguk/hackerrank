from typing import List
from collections import Counter

def count_triples(arr,r):
    c = 0
    right = Counter(arr)
    left = Counter()
    for elem in arr:
        # remove from right
        right[elem] -= 1
        if elem % r == 0:
            lc = left[elem // r]
            rc = right[elem *r]
            c += (lc*rc)
        left[elem] += 1
    print(c)

def main():
    t1 = [1,3,9,9,27,81]
    count_triples(t1,3)
    return 0

if __name__ =="__main__":
    main()