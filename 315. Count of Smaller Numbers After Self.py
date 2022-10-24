import bisect

nums = [5, 2, 6, 1, 5]

count = 0
ans = []

sorted_num = sorted(nums)
for num in nums:
    c = bisect.bisect_left(sorted_num, num)
    ans.append(c)
    del sorted_num[c]
print(ans)
