from typing import List
from collections import Counter

def note(m,n):
    
    mc = Counter(m)
    nc = Counter(n)
    # for k,v in nc.items():
    #     if mc[k] < v:
    #         print("No")
    #         return
    # print("Yes")
    # return
    if all( [mc[k] >= v for k,v in nc.items()]):
        print("Yes")
    else:
        print("No")
    return
def main():
    m1 = ["two","times","three","is","four"]
    n1 = ["two","times","three","is","four"]
    # a = [1,2,3]
    # b = [2,4]
    # if all([x in a for x in b]):
    #     print("Yes")
    # else:
    #     print("No")
    note(m1,n1)
    return 0

if __name__ =="__main__":
    main()