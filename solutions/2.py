"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
---
Answer is 4613732
"""

MAX = 4_000_000

fib1, fib2 = 2, 1
ans = 0

while fib1 <= MAX:
    if fib1 % 2 == 0:
        ans += fib1

    fib1, fib2 = fib1 + fib2, fib1

print(ans)
