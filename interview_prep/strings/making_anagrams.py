from collections import Counter


def make_anagrams(a,b):
    ac = Counter(a)
    bc = Counter(b)
    deletions = 0
    all_chars = set(ac.elements()).union(bc.elements())
    for char in all_chars:
        deletions += abs(ac[char] - bc[char])
    # print(deletions)
    
    return deletions

def main():
    a = "cde"
    b = "abc"
    print(make_anagrams(a,b))
    return 0

if __name__ == "__main__":
    main()
    

