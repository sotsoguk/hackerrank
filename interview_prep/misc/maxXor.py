from typing import List
import sys, math

# def maxXor(arr, queries):
#     max_vals=[]
#     for q in queries:
#         m = 0
#         for i in arr:
#             m = max(m,i^q)
#         max_vals.append(m)
#     return max_vals


def maxXor(arr,queries):
    # find max bit length of all entries
    bl = max(max(map(lambda x:math.floor(math.log(x,2)),arr)),max(map(lambda x:math.floor(math.log(x,2)),queries)))+1
    mask = 2**(bl)
    ones = []
    zeroes = []
    for i in range(bl):
        ones.append([])
        zeroes.append([])
    for i in range(bl):
        mask >>= 1
        for a in arr:
            if mask & a == mask:
                ones[i].append(a)
            else:
                zeroes[i].append(a)
        print(mask)
   # print(bl)
    print(ones,zeroes)
    return
# def maxXor(arr, queries):

#     max_vals=[]
#     arr_or = 0
#     for i in arr:
#         arr_or |= i
#     for q in queries:
        
#         m = q ^ arr_or
#         max_vals.append(m)
#     return max_vals
def main():
    # a1 = [0,1,2]
    # q1 = [3,7,2]
    a1 = [3,4,8]
    q1 = [7,6]
    #print(maxXor(a1,q1))
    maxXor(a1,q1)
    # print(max(map(lambda x:math.ceil(math.log(x,2)),q1)))
    # print(math.ceil(math.log(7,2)))
    return 0
if __name__ == "__main__":
    main()
