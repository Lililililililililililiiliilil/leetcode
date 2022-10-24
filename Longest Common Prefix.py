strs = ["flower", "flow", "flight"]


def lcp(strs):
    ans = ""
    for i in range(len(strs[0])):
        for word in strs:
            if i >= len(word) or word[i] != strs[0][i]:
                return ans
        ans += strs[0][i]
    return ans


print(lcp(strs))
