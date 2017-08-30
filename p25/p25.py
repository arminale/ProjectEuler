bignum = 10 ** 999
left = 1
right = 1
index = 2
while right < bignum:
    index += 1
    left, right = right, right + left
print(index)