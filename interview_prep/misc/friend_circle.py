from typing import DefaultDict, List
from collections import Counter, defaultdict
import sys

def query(f,a,b):
    minIdx, maxIdx = 0,0
    if f[a] != 0:
        a = f[a]
    if f[b] != 0:
        b = f[b]
    
    if a<b:
        minIdx = a
        maxIdx = b
    else:
        minIdx = b
        maxIdx = a
    
    f[a]=maxIdx
    f[b]=maxIdx
    for k,v in f.items():
        if v == minIdx:
            f[k] = maxIdx

def solve(queries:List[int]) ->List[int]:
    max_friends = 10
    members = [[] for i in range(max_friends)]
    groups = [0] * max_friends
    friend_id = defaultdict(lambda: len(friend_id))
    m = 2
    k = 0
    output = []
    
    for l,r in queries:
        # print(l,r,end="|")
        l = friend_id[l]
        r = friend_id[r]
        # print(l,r,end="|| ")
        # print((ref))

        a = groups[l]
        b = groups[r]
        if a == 0 and b==0:
            k += 1
            groups[l] =k
            groups[r] = k
            members[k].append(l)
            members[k].append(r)
        elif a == 0:
            groups[l] = b
            members[b].append(l)
            m = max(m,len(members[b]))
        elif b == 0:
            groups[r] = a
            members[a].append(r)
            m = max(m,len(members[a]))
        elif a==b:
            pass
        elif len(members[a]) >len(members[b]):
            #merge
            members[a].extend(members[b])
            for i in members[b]:
                groups[i] = a
            members[b] = None
            m = max(m,len(members[a]))
        else:
            #merge
            members[b].extend(members[a])
            for i in members[a]:
                groups[i] = b
            members[a] = None
            m = max(m,len(members[b]))
        print(m)
        output.append(m)

    return output
def largest_circle(f):
    c = Counter(f.values())
    return c.most_common(1)[0][1]
def main():

    # f = DefaultDict(int)
    # query(f,1,2)
    # print(largest_circle(f))
    # query(f,3,4)
    # print(largest_circle(f))
    # query(f,1,3)
    # print(largest_circle(f))
    # query(f,5,7)
    # print(largest_circle(f))
    # query(f,5,6)
    # print(largest_circle(f))
    # query(f,7,4)
    # print(largest_circle(f))
    
    #q = [[1,2],[3,4],[1,3],[5,7],[5,6],[7,4]]
    q = [[6,4],[5,9],[8,5],[4,1],[1,5],[7,2],[4,2],[7,6]]
    
    res = solve(q)


if __name__ == "__main__":
    main()
