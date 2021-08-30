def sc_rec(n,idx):
    m = 10**10 + 7
    if idx > n:
        return 0
    if idx == n:
        return 1
    if idx == (n-1):
        return 1
    if idx == (n-2):
        return 2
    if idx == (n-3):
        return 4

    return (sc_rec(n,idx+1) % m) + sc_rec(n,idx+2) % m + sc_rec(n,idx+3) % m

# def staircase(n):
#     return sc_rec(n,0)

def staircase(n):
    n1,n2,n3 = 1,2,4
    if n == 1:
        return n1
    if n == 2:
        return n2
    if n == 3:
        return n3
    steps = 0
    
    for i in range(4,n+1):
        steps = n1+n2+n3
        n1 = n2
        n2 = n3
        n3 = steps
    return steps
def main():
    
    print(staircase(34))
if __name__ == "__main__":
    main()