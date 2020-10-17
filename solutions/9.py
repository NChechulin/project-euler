"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
-----
Answer: 31875000
"""


def is_pyth_triplet(a, b, c):
    return a*a + b*b == c*c


for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b

        if is_pyth_triplet(a, b, c):
            print(a * b * c)
            exit()
