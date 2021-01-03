# Given a collection of distinct integers, return all possible permutations.

# [1,2,3]

# Output: [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
# first Solution
lst = [1, 2, 3]
p = [[]]
for i in range(len(lst)):
    p = [[a] + b for a in lst for b in p if a not in b]
print(p)

