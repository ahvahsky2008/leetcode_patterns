def calc_sum_subarray_of_size_k(arr, k):
    wstart = 0
    wsum = 0
    maxsum = 0
    
    for wend in range(len(arr)):
        wsum += arr[wend]
        if wend >= k-1:
            maxsum = max(maxsum, wsum)
            wsum -= arr[wstart]
            wstart+=1
    
    return maxsum

input = [2, 1, 5, 1, 3, 2]
result = calc_sum_subarray_of_size_k(input, k=3)
assert result == 9