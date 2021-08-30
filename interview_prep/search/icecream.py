def whatIce(cost,money):
    # create dict
    cdict = dict()
    for i,c in enumerate(cost):
        cdict[c] = i

    print(cdict)
    for i,c in enumerate(cost):
        if (money-c) in cdict.keys() and cdict[money-c] != i:
            print(min(cdict[money-c],i)+1,max(cdict[money-c],i)+1)
            return

def main():
    t1 = [2,1,3,5,6]
    whatIce(t1,5)
    return 0

if __name__ == "__main__":
    main()