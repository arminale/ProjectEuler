# https://projecteuler.net/problem=112 bouncy numbers


def is_bouncy(num):

    has_incr_seq, has_decr_seq = False, False
    right = num % 10
    num = num // 10

    while num > 0:
        left = num % 10
        if left < right:
            has_incr_seq = True
        elif left > right:
            has_decr_seq = True
        right = left
        num = num // 10
        if has_incr_seq and has_decr_seq:
            return True
    return False


count = 0
i = 99

while count < 0.99 * i:
    i += 1
    if is_bouncy(i):
        count += + 1
print(i)