from collections import defaultdict

def steady_gene(gene):
    def issteady():
        return all([cnt[x] <= exp_num for x in gs])

    # first, parse the genome and count the numbers
    min_len = len(gene)
    gs = {'A','C','G','T'}
    cnt = defaultdict(int)
    for g in gene:
        cnt[g] += 1
    
    # expected
    exp_num = len(gene) // 4
    if issteady():
        return 0
    
    hp, tp = 0,0

    while hp < len(gene):
        cnt[gene[hp]] -= 1
        hp +=1

        if issteady():
            min_len = min(min_len,hp-tp-1)
            while tp <= hp and issteady():
                cnt[gene[tp]] += 1
                if issteady():
                    min_len = min(min_len,hp-tp-1)
                    tp += 1
                else:
                    cnt[gene[tp]] -=1
                    break
    return min_len
    
def main():
    print(steady_gene("GAAATAAA"))
    print(steady_gene("ACGCCTGA"))
    return 0

if __name__ == "__main__":
    main()