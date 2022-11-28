from typing import List


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    winners = dict()
    losers = dict()
    ans = [[], []]
    for match in matches:
        if match[0] in winners:
            winners[match[0]] += 1
        else:
            winners[match[0]] = 1
        if match[1] in losers:
            losers[match[1]] += 1
        else:
            losers[match[1]] = 1
    for keys in losers:
        if losers[keys] == 1:
            ans[1].append(keys)
    for keys in winners:
        if keys not in losers.keys():
            ans[0].append(keys)
    ans[0].sort()
    ans[1].sort()
    return ans


matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
print(findWinners(matches))
