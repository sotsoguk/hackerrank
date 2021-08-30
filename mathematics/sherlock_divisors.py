import math

def divisors(n):
    if n%2 != 0:
        return 0
    cnt = 1
    m = n//2
    while m>1:
        if m % 2 == 0:
            cnt +=1
            m //=2
        elif (n/m)%2 == 0:
            cnt +=1
            m = (n/m)//2
        else:
            return cnt
    return cnt


def main():
    for i in range(1,101):
        print(i,divisors(i))
    return 0

if __name__ == "__main__":
    main()