"""
What is the largest prime factor of the number 600851475143 ?
"""

N = 600851475143

ans = 1

k = 2
while N != 1:
    while N % k == 0:
        N //= k
        ans = k
    k += 1

print(ans)
