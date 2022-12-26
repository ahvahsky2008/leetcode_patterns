import math
def calc_smallest_subarray_of_given_summ(arr, s):
    window_start=0
    window_sum = 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum +=arr[window_end]
        print(window_sum)

        while window_sum >=s:
            min_length = min(min_length, window_end-window_start+1)
            window_sum -= arr[window_start]
            window_start += 1
        
    if min_length == math.inf:
        return 0
    return min_length
            
input =  [2, 1, 5, 2, 8] #7
result = calc_smallest_subarray_of_given_summ(input, s=7)
assert result == 2
