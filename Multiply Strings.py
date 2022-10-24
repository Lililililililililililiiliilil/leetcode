num1 = "132"
num2 = "3"

strToInt = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

rightNum1 = 0
rightNum2 = 0

for i in num1:
    print(i)
    rightNum1 = rightNum1 * 10 + strToInt.get(i)
    print(rightNum1)

for i in num2:
    rightNum2 = rightNum2 * 10 + strToInt.get(i)


