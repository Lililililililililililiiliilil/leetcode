num = input()


def digitCount(num: str):
    for i in range(len(num)):
        if num.count(str(i)) == int(num[i]):
            continue
        else:
            return False
    return True


print(digitCount(num))
print(num.count(str(0)))
