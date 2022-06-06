def fruits_in_baskets(string):
    wstart = 0 
    wmax = 0
    d = {}

    for wend in range(len(string)):
        if string[wend] not in d:
            d[string[wend]]  = 0
        d[string[wend]] += 1
       
        while len(d)>2:
            d[string[wstart]]-=1
            if d[string[wstart]] == 0:
                del d[string[wstart]]

            wstart+=1            
        wmax =max(wmax, wend - wstart + 1)
    return wmax

x = fruits_in_baskets(['A', 'B', 'C', 'B','B', 'C'])
print(x)

