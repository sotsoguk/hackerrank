from typing import List
from collections import Counter

def anagrams(s):
    # find all substrings
    all_subs = []
    for i in range(1,len(s)):
        for j in range(0,len(s)+1-i):
            all_subs.append("".join(sorted(s[j:j+i])))
    #print(all_subs)
    # all_subs_sorted = "".join(map(lambda x:sorted(x),all_subs))
    # print(all_subs_sorted)
    # only substrings which appear at least twice can be used
    count = {k:v for k,v in Counter(all_subs).items() if v > 1}
    # print(count)
    # print(count.values())
    # if a substring occurs n times, 
    # 1+2+...+(n-1) pairs of anagrams can be created
    #print(sum(sum(range(i)) for i in count.values()))
    return (sum((i*(i-1))//2 for i in count.values()))
def main():
    t1= "abba"
    anagrams(t1)
    return 0

if __name__ =="__main__":
    main()