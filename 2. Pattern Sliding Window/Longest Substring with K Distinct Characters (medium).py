import math
def longest_substring_with_k_distinct(string, k):
    window_start = 0
    max_length = 0
    hashamp = {}

    for window_end in range(len(string)):
        
        
        char_end = string[window_end] # 'c' ,'b'
        if char_end not in hashamp:
            hashamp[char_end] = 0
        
        hashamp[char_end] += 1  # {c:1, b:2 }
        
                
        while len(hashamp.keys())>2:
            
            char_start = string[window_start] # 'c'
            
            hashamp[char_start] -=1
            if hashamp[char_start] == 0:
                del hashamp[char_start]
            
            window_start+=1
        max_length = max(max_length, window_end - window_start + 1)
                    
    return max_length
        
'''
cbbebi

'''
 
x = longest_substring_with_k_distinct('cbbebi',3)
print(x)

