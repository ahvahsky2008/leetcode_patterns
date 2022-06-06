def no_repeat_substring(string):
    charset = set()
    l = 0
    res = 0

    for r in range(len(string)):
        while string[r] in charset:
            charset.remove(string[l])
            l+=1
        charset.add(string[r])
        res = max(res, r - l + 1)
    
    return res

x = no_repeat_substring("abcabcbb")
print(x)

