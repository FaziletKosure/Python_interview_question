
def closing_in_sum(n):
    x = [i for i in str(n)]  # [2, 5, 2, 0]
    count = 0
    for i in range(len(x)//2):
        count += int(x[i]+x[-1-i])
    if len(x) % 2:
        count += int(x[len(x)//2])
    return count


closing_in_sum(251220)  # 72

# The first and last digits are 2 and 0.
# 2 and 0 form 20.
# The second and second to last digits are 5 and 2.
# 5 and 2 form 52.

# 20 + 52 = 72



def closing_in_sum1(n):
    n = str(n)
    if len(n) <= 2:
        return int(n)
    return int(n[0] + n[-1]) + closing_in_sum1(n[1:-1])
