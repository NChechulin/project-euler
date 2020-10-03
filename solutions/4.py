"""
Find the largest palindrome made from the product of two 3-digit numbers.
---
Answer is 906609
"""


def is_palindrome(x: int) -> bool:
    x = str(x)

    return x == x[::-1]


ans = -1

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        if is_palindrome(a * b):
            ans = max(ans, a * b)

print(ans)
