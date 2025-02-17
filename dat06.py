def is_even(n) -> bool:

    # if n % 2 == 0:?><1
    #     return True
    # return False
    return not n & 1


n = int(input())
print(is_even(n))