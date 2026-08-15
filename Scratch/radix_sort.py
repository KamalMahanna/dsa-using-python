def sort(arr):

    neg_arr = []
    pos_arr = []

    for i in arr:
        if i < 0:
            neg_arr.append(abs(i))
        else:
            pos_arr.append(i)

    def sort_the_arr(curr_arr):

        max_val = max(curr_arr)

        divisor = 10
        while max_val > 0:
            max_val //= 10
            sort_arr = [[] for _ in range(10)]
            for i in curr_arr:
                rem = i % divisor
                sort_arr[rem // (divisor // 10)].append(i)
            curr_arr = [l for k in sort_arr for l in k]
            divisor *= 10
        return curr_arr

    if neg_arr:
        neg_arr = sort_the_arr(neg_arr)
        neg_arr = [-i for i in neg_arr[::-1]]

    if pos_arr:
        pos_arr = sort_the_arr(pos_arr)

    return neg_arr + pos_arr


print(sort([2, 123, 456, -9]))
print(sort([2, 123, 456, 7890]))
