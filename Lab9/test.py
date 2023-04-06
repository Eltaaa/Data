import random

# print(random.sample(range(1, 11), 10))
x = [8, 9, 2, 1, 3, 4, 10, 7, 5, 6]


x[0], x[1] = x[1], x[0]
print(x)