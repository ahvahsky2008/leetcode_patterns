def calc_sum_subarray_of_size_k(arr, k):
    wstart=0
    wsum=0
    max_sum = 0

    for index in range(len(arr)):
        wsum += arr[index]

        if index >= k-1:
            max_sum = max(max_sum, wsum)
            wsum -= arr[wstart]
            wstart+=1
    return max_sum


input = [2, 1, 5, 1, 3, 2]
result = calc_sum_subarray_of_size_k(input, k=3)
assert result == 9