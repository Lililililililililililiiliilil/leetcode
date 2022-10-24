nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

ans = list(range(len(nums) + 1))

for num in nums:
    ans.remove(num)

print(*ans)
