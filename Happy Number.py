n = int(input())


def squared_sum(n):
    ans = 0
    while n != 0:
        ans += (n % 10) ** 2
        n //= 10
    return ans


prev = []
while n != 1:
    n = squared_sum(n)
    if n in prev:
        print('false', n)
    else:
        prev.append(n)
