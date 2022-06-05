import math
def calc_smallest_subarray_of_given_summ(arr, s):
    window_start = 0
    window_summ = 0
    window_min = math.inf

    for window_end in range(len(arr)):
        window_summ += arr[window_end]
        while window_summ >= s:
            window_min = min(window_min,window_end - window_start + 1)
            window_summ -= arr[window_start]
            window_start+=1
    if window_min == math.inf:
        return 0
    return window_min

            
input =  [2, 1, 5, 2, 8] #7
result = calc_smallest_subarray_of_given_summ(input, s=7)
assert result == 1