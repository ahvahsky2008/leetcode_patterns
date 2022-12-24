def calc_sum_subarray_of_size_k(arr, k):
    window_sum = 0
    max_sum = 0
    
    for i in range(len(arr)):
        window_sum+=arr[i]
        
        if i>=k:
            window_sum = window_sum-arr[i-k]
        
        max_sum = max(window_sum,max_sum)        
    
    return max_sum  

input = [2,3,4,1,5]
result = calc_sum_subarray_of_size_k(input, k=2)
assert result == 7
