# Given n pairs of parentheses, write a code to generate all combinations of well-formed (valid for Python) parentheses.
# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


n = 3
r = ["()"]
for _ in range(n-1):
    r = [i[0:j+1]+"()"+i[j+1:] for i in r for j in range(len(i))]
    r = list(dict.fromkeys(r))
print(r)
