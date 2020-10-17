"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
-----
Answer: 25164150
"""

N = 100

sum_of_squares = sum(i*i for i in range(N + 1))
square_of_sum = (N*(N + 1) // 2) ** 2

print(abs(square_of_sum - sum_of_squares))
