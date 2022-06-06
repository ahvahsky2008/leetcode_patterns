
def longest_substring_with_k_distinct(string, k):
    wstart = 0 
    wmax = 0
    d = {}

    for wend in range(len(string)):
        if string[wend] not in d:
            d[string[wend]]  = 0
        d[string[wend]] += 1
       
        while len(d)>k:
            d[string[wstart]]-=1
            if d[string[wstart]] == 0:
                del d[string[wstart]]

            wstart+=1            
        wmax =max(wmax, wend - wstart + 1)
    return wmax

x = longest_substring_with_k_distinct('aabacbebebe',3)
print(x)

