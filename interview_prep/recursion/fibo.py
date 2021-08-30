def fibo(n):
    if n<1:
        return 0
    if n in [1,2]:
        return 1
    fn,fnn = 0,1
    for i in range(n):
        # tmp = fnn
        # fnn += fn
        # fn = tmp
        fnn, fn = fnn+fn, fnn
        print(fn,fnn)
    print(fn)

def main():
    fibo(5)

if __name__ == "__main__":
    main()