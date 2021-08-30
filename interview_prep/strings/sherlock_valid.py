from collections import Counter
def valid_string(s):
    # c = Counter(s)
    # print(c)
    # mc = (Counter(c.values()).most_common(1))[0][0]
    # one_a = sum([abs(e-mc) for e in c.values()])
    # bb = sum([1 if e!=mc and e==1 else 0 for e in c.values()])
    # print(bb)
    # if one_a <= 1 or bb == 1:
    #     return "YES"
    # else:
        
    #     return "NO"
    # print(one_a)
    y = "YES"
    n = "NO"
    c = Counter(Counter(s).values())
    if len(c) == 1: # all characters appear the same number of times
        return y
    elif len(c) >2: # more than one character is "off"
        return n
    # if one character is off it either has to be one occurance more or less or it appears once, so can be deleted
    elif 1 in c.values() and ( max(c.keys()) - min(c.keys()) == 1 or c[min(c.keys())] == 1 ):
        return y
    else:
         return n
def main():
    t1 = "abcc"
    t2 = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"
    t3 = "xxxaabbccrry"
    print(valid_string(t3))
    return 0

if __name__ == "__main__":
    main()