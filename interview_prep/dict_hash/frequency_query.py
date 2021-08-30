from typing import List
from collections import Counter, defaultdict

def freq(queries):
    output = []
    d = defaultdict(int)
    c = defaultdict(int)
    for q in queries:
        if q[0] == 1:
            c[d[q[1]]] -=1
            d[q[1]] +=1
            c[d[q[1]]] +=1
        elif q[0] == 2:
            if d[q[1]] > 0:
                c[d[q[1]]] -=1
                d[q[1]] -= 1
                c[d[q[1]]] +=1
        else:
            z = q[1]
            #if any([v == z for v in d.values()]):
            if c[z] > 0:
                output.append(1)
            else:
                output.append(0)
            yield 1 if c[z] 
        # print(d)
    return output

def main():
    t1 = [[1,5],[1,6],[3,2],[1,10],[1,10],[1,6],[2,5],[3,2]]
    print(freq(t1))
    return 0

if __name__ =="__main__":
    main()