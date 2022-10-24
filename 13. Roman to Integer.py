s = "MDCXCV"

numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

ans = 0
i = 0
flag = True

while i < len(s):
    if i < len(s) - 1:
        if numbers.get(s[i]) < numbers.get(s[i + 1]):
            ans += numbers.get(s[i + 1]) - numbers.get(s[i])

            i += 2
            flag = False
        else:
            ans += numbers.get(s[i])
            i += 1
            flag = True
    else:
        ans += numbers.get(s[i])
        i += 1
        flag = True

print(ans)
