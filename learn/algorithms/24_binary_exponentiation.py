"""
Binary Exponentiation (also known as exponentiation by squaring) is an efficient way to compute large powers.
It reduces the number of multiplications from O(n) to O(log n) by using the property that a^n = (a^(n/2))^2.
"""


def power(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res *= a
        a *= a
        b //= 2
    return res


if __name__ == "__main__":
    print(f"2^10 = {power(2, 10)}")
