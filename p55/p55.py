count = 0
for i in range(1, 10001):
    num = i
    isPal = False
    for j in range(50):
        num += int(str(num)[::-1])
        isPal = str(num) == str(num)[::-1]
        if isPal:
            break
    if not isPal:
        count += 1
print(count)