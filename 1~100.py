def sum_diff_to_N(N):
    sum_score=0
    item = 2
    while item <= N:
        if item % 2 == 0:
            sum_score+= item
        else:
            sum_score -= item
        item += 1
    return sum_score
print(sum_diff_to_N(5))