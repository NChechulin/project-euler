"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
------
Answer: 232792560
"""


from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


ans = 1

for i in range(2, 20):
    ans = lcm(ans, i)

print(ans)
