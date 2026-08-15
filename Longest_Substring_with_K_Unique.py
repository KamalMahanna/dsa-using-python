def longestKSubstr(s, k):

    char_cntr = {}
    p1 = 0
    max_sub = 0
    unq_char_cnt = 0
    for p2 in range(len(s)):
        if char_cntr.get(s[p2], 0) == 0:
            unq_char_cnt += unq_char_cnt

        char_cntr[s[p2]] = char_cntr.get(s[p2], 0) + 1

        while unq_char_cnt > k:
            char_cntr[s[p1]] = char_cntr[s[p1]] - 1
            if char_cntr[s[p1]] == 0:
                unq_char_cnt -= 1
            p1 += 1

        if unq_char_cnt == k:
            max_sub = max(max_sub, p2 - p1 + 1)
    return -1 if max_sub == 0 else max_sub


print(longestKSubstr("aabacbebebe", 3))
