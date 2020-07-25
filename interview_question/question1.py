# Interview Question by : Google, Adobe, Facebook, Cisco, Microsoft
# ----------------------------
# Group Anagrams
# Given a list of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: :bangbang:
# All inputs will be in lowercase.
# The order of your output does not matter.


def group_anagrams(input):
    # start an empty dictionary to hold the values
    my_dict = {}
    # loop through list of strings
    for s in input:
        key = ''.join(sorted(s))
        # print(key)  #'aet'
        # check if key exist in dictionary or not.
        # If yes append the s into the list of corresponding key.
        # If not then start an empty list on the key and then append values
        if key in my_dict.keys():
            my_dict[key].append(s)
        else:
            my_dict[key] = []
            my_dict[key].append(s)
    # print(my_dict)
    # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
    return list(my_dict.values())


xx = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(xx))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
